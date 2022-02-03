import re


def json2bibtex(json_data):

    template = '@article{AUTHORYEAR,\n \
    title = {{TITLE}},\n \
    author = {AUTHORSLST},\n \
    journal = {JOURNAL},\n \
    volume = {VOLUME},\n \
    number = {NUMBER},\n \
    pages = {PAGES},\n \
    year = {PUBYEAR},\n}'

    medline = json_data['PubmedArticle'][0]['MedlineCitation']['Article']

    bibtex = template

    ### Authors list
    authorsLst = []

    try:
        for author in medline['AuthorList']:
            try:
                authorsLst.append(author['LastName'] + ' ' + author['Initials'])
            except:
                pass
    except:
        pass

    if len(authorsLst) == 0:
        try:
            authorsLst.append(medline['AuthorList'][0]['CollectiveName'])
        except:
            pass

    authorsLst = ' and '.join(authorsLst)
    bibtex = bibtex.replace('AUTHORSLST', authorsLst)

    ### Title
    title = medline['ArticleTitle']
    bibtex = bibtex.replace('TITLE', title)

    ### Journal
    journal = medline['Journal']['Title']
    bibtex = bibtex.replace('JOURNAL', journal)
    #print(medline['Journal']['ISOAbbreviation'])

    ### Year
    try:
        year = medline['Journal']['JournalIssue']['PubDate']['Year']
    except:
        year = medline['Journal']['JournalIssue']['PubDate']['MedlineDate']

    bibtex = bibtex.replace('PUBYEAR', year)

    ### Bibtex header NameYear
    try:
        author = medline['AuthorList'][0]['LastName']
    except:
        try:
            author = medline['AuthorList'][0]['CollectiveName'].replace(' ', '')
        except:
            author = str()

    authoryear = re.sub(r'[^A-Za-z0-9]', '', author + year + title.split()[0])
    bibtex = bibtex.replace('AUTHORYEAR', authoryear)

    ### Number (Issue)
    try:
        number = medline['Journal']['JournalIssue']['Issue']
        bibtex = bibtex.replace('NUMBER', number)
    except:
        bibtex = [x for x in bibtex.splitlines() if 'number = ' not in x]
        bibtex = '\n'.join(bibtex)

    ### Volume
    try:
        volume = medline['Journal']['JournalIssue']['Volume']
        bibtex = bibtex.replace('VOLUME', volume)
    except:
        bibtex = [x for x in bibtex.splitlines() if 'volume = ' not in x]
        bibtex = '\n'.join(bibtex)

    ### Pages
    try:
        pages = medline['Pagination']['MedlinePgn']
        bibtex = bibtex.replace('PAGES', pages)
    except:
        bibtex = [x for x in bibtex.splitlines() if 'pages = ' not in x]
        bibtex = '\n'.join(bibtex)

    bibtex = bibtex.replace('&', '\&')

    return bibtex

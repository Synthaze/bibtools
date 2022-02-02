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

    for author in medline['AuthorList']:
        try:
            authorsLst.append(author['LastName'] + ' ' + author['Initials'])
        except:
            pass
            
    if len(authorsLst) == 0:
        authorsLst.append(medline['AuthorList'][0]['CollectiveName'])

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
    year = medline['Journal']['JournalIssue']['PubDate']['Year']
    bibtex = bibtex.replace('PUBYEAR', year)

    ### Bibtex header NameYear
    try:
        author = medline['AuthorList'][0]['LastName']
    except:
        author = medline['AuthorList'][0]['CollectiveName'].replace(' ', '')
        
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

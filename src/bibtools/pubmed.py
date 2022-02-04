#
from utilsovs import fetch_one_PubMed
from utilsovs.pubmed import altsearch_MedLine_API
from pybasics import write_json, write_file
import requests
import re
import os


class PubMed:

    url = 'https://pubmed.ncbi.nlm.nih.gov/'

    pmc = 'https://www.ncbi.nlm.nih.gov/pmc/articles/'

    headers = {
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-gpc': '1',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-US,en;q=0.9',
    }

    def __init__(self, storage):

        self.storage = storage

        return None

    def search(self, request=None):

        print('PubMed.search(): start')

        self.results = altsearch_MedLine_API(request=request, db='pubmed')

        print('PubMed.search(): end')

        return None

    def fetch(self, _id):

        print('PubMed.fetch(): start')

        self.json = fetch_one_PubMed(_id).data

        Article = self.json['PubmedArticle'][0]['MedlineCitation']['Article']

        try:
            self.doi = Article['ELocationID'][0]
        except:
            try:
                self.doi = self.json['PubmedArticle'][0]['PubmedData']['ArticleIdList'][-1]
            except:
                self.doi = False

        self.pmcid = self.json['PubmedArticle'][0]['PubmedData']['ArticleIdList'][-1]
        self.pmcid = self.pmcid if 'PMC' in self.pmcid else None

        self.pmid = _id

        self.fetch_url = self.url + self.pmid

        self.RawArticleTitle = Article['ArticleTitle']
        self.ArticleTitle = re.sub(r'[^A-Za-z0-9]', '_', Article['ArticleTitle'])

        try:
            self.ArticleDate_Year = Article['Journal']['JournalIssue']['PubDate']['Year']
        except:
            self.ArticleDate_Year = Article['Journal']['JournalIssue']['PubDate']['MedlineDate']

        try:
            self.FirstAuthor = Article['AuthorList'][0]['LastName']
        except:
            try:
                self.FirstAuthor = Article['AuthorList'][0]['CollectiveName'].replace(' ', '')
            except:
                self.FirstAuthor = str()
        self.fname = self.FirstAuthor + self.ArticleDate_Year + '_' + self.ArticleTitle + '_' + self.pmid
        self.fname = re.sub(r'[_]+', '_', self.fname)

        if len(self.storage + self.fname) >= 250:
            max_length = 250 - len(self.pmid) - 4
            self.fname = '_'.join(self.fname.split('_')[:-1])[:max_length] + '_TR_' + self.pmid

        self.fname = os.path.join(self.storage, self.fname)

        write_json(self.fname + '.json', self.json)

        print('PubMed.fetch(): end')

        return None

    def download(self, _id):

        print('PubMed.download(): start')

        url = self.pmc + self.pmcid + '/pdf/'

        link = url + requests.get(url).text.split(url)[1].split('</div>')[0] + '?download=true'

        self.pdf = requests.get(link, headers=self.headers)

        write_file(self.fname + '.pdf', self.pdf.content, mode='wb')

        print('PubMed.download(): end')

        return None

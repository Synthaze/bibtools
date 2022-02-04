#
import re
import os
import requests
from pybasics import write_file
from bibtools.utils import scrapper


class SciHub:

    scheme = 'https://'

    links = [
        'sci-hub.mksa.top',
    ]

    headers = {
        'authority': None,
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'origin': None,
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-gpc': '1',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': None,
        'accept-language': 'en-US,en;q=0.9',
    }

    data = {
      'request': None,
    }

    def __init__(self):

        pass

        return None

    def download(self, doi=None, pmid=None, fname=None):

        print('SciHub.download(): start')

        for link in self.links:

            url = self.scheme + link

            self.headers['authority'] = link
            self.headers['origin'] = url
            self.headers['referer'] = url

            if doi:
                self.data['request'] = 'https://doi.org/' + doi
            else:
                self.data['request'] = 'https://pubmed.ncbi.nlm.nih.gov/' + pmid

            response = requests.post(url=url, headers=self.headers, data=self.data)

            pdf = scrapper(url, response)

            self.pdf = requests.get(url=pdf, headers=self.headers)

            write_file(fname, self.pdf.content, mode='wb')

        print('SciHub.download(): end')

        return None

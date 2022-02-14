#
from pybasics import read_file
from bibtools.formatters import alpha
import sys
import os


help = [
'bibtools\n',
'https://github.com/synthaze/bibtools <florian.malard@gmail.com>\n',
'Usage:',
'  bibtools OPTION...\n',
'Options:',
'  -h, --help             show help',
'  -i, --input=STRING     comma-separated PMIDs or DOIs',
'  -l, --list=FILE        list of PMIDs or DOIs, one per line',
'  -p, --path=STRING      path where to write files',
#'  -f, --format=STRING    ',
'  -b, --bibtex           write bibtex files',
'  -c, --cite             print latex style TITLE~\cite{header}',
'  -a, --abstract         print latex style ABSTRACT~\cite{header}',
]

def argparse(argv):

    del argv[0]

    if argv[0] in ['-h', '--help']:
        print('\n'.join(help))
        sys.exit()

    storage = os.getcwd()

    formatter = None

    bibtex = True if '-b' in argv or '--bibtex' in argv else False
    cite = True if '-c' in argv or '--cite' in argv else False
    abstract = True if '-a' in argv or '--abstract' in argv else False
    
    argv = [argv for argv in argv if argv not in ['-b', '--bibtex', '-c', '--cite', '-a', '--abstract']]

    for i in range(0, len(argv), 2):

        if argv[i] in ['-f', '--format']:
            if argv[i + 1] == 'alpha':
                formatter = alpha

        elif argv[i] in ['-i', '--input']:
            data = argv[i + 1].split(',')

        elif argv[i] in ['-l', '--list']:
            data = read_file(argv[i + 1], True)

        elif argv[i] in ['-p', '--path']:
            storage = argv[i + 1]

    return data, storage, formatter, bibtex, cite, abstract


def scrapper(url, response):
    try:
        link = response.text.split('onclick="location.href=')[1].split('>')[0].strip('"').strip("'")
        link = link.replace('\\', '')
        return link
    except:
        pass

    try:
        return url + response.text.split('pdf.bban.top')[1].split('>')[0]
    except:
        pass

    return None

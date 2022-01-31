#
import re


def alpha(reference):
    """
    Format query for:
    Martinez-Rucobo, F.W., et al. Mol Cell, 2015. 58(6):1079-89.
    """
    reference = reference.replace('et al', '')
    reference = re.split(r',', reference)

    del reference[1]

    reference[1] = re.sub('[^A-Za-z0-9\s]', '', reference[1]).strip()

    reference[1] = reference[1].strip().replace(' ', '+')
    reference = [x.strip() for x in reference]

    reference[0] = reference[0] + '[Author%-%First]'

    reference = ' '.join(reference)
    reference = reference.replace(' ', ' AND ')
    reference = reference.replace('%', ' ')

    return reference

# bibtools - 0.1

Retrieve papers and metadata from the command-line.

Intended for papers referenced in MedLine/PubMed.

## Install

    pip3 install bibtools-pkg

## Use

### Generic

Returns exact matches when using unique identifiers (PMID, DOI).

Fetch PubMed Central for open-access papers as well as Sci-Hub:

    bibtools -i PMID # Single PMID or DOI

    bibtools -i PMID1,PMID2 # Comma-separated PMIDs and/or DOIs

    bibtools -i pmids.dat # List file of PMIDs (or DOIs), one per line

    bibtools -i PMID -b # Generate bibtex from MedLine citation data

    bibtools -i PMID -p /path/to/directory # With custom storage path. Default is current working directory

### Examples

Working calls:

    bibtools -i 25809265

    bibtools -i 10.1016/j.bpj.2015.01.032

    bibtools -i 25809265,10.1016/j.jmr.2007.04.002

    bibtools -i 25809265,10.1016/j.jmr.2007.04.002 -b -c

## Help

To show help:

    bibtools -h

Which returns:

    bibtools

    https://github.com/synthaze/bibtools <florian.malard@gmail.com>

    Usage:
      bibtools OPTION...

    Options:
      -h, --help             show help
      -i, --input=STRING     comma-separated PMIDs or DOIs
      -l, --list=FILE        list of PMIDs or DOIs, one per line
      -p, --path=STRING      path where to write files
      -b, --bibtex           write bibtex files
      -c, --cite             print latex style TITLE~\cite{header}

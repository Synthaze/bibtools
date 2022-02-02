# bibtools - 0.1

Retrieve papers and metadata from the command-line.

Intended for papers referenced in MedLine/PubMed.

Install:

    pip3 install bibtools-pkg

Returns exact matches when using unique identifiers (PMID, DOI).

Fetch PubMed Central for open-access papers as well as Sci-Hub:

    bibtools -i PMID # Single PMID or DOI

    bibtools -i PMID1,PMID2 # Comma-separated PMIDs and/or DOIs

    bibtools -l pmids.dat # List file of PMIDs (or DOIs), one per line

    bibtools -i PMID -b # Generate bibtex from MedLine citation data

    bibtools -i PMID -p /path/to/directory # With custom storage path. Default is current working directory


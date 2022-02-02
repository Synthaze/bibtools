# bibtools - 0.1

Install:

    pip3 install bibtools-pkg

Fetch PubMed Central for open-access papers as well as Sci-Hub

    bibtools -i PMID # Single PMID

    bibtools -i PMID1,PMID2 # Comma-separated PMIDs

    bibtools -l pmids.dat # List file of PMIDs, one per line
    
    bibtools -i PMID -b # Generate bibtex from MedLine json
    
    bibtools -i PMID -p /path/to/directory # With custom storage path. Default is current working directory
    
While untested, may work with DOIs and other unique identifiers.

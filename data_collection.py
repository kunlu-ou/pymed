# searching a database
# Example: Get the PubMed IDs (PMIDs) for articles about breast cancer published in Science in 2008
# https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=science[journal]+AND+breast+cancer+AND+2008[pdat]
import csv
from pymed import PubMed

# a list of check tags in MeSH: https://www.nlm.nih.gov/bsd/indexing/training/CHK_010.html


pubmed = PubMed(tool="DataCollection", email="kunlu@ou.edu")
# Create a GraphQL query in plain text
query = '(1990/01/01:2022/12/31[Date - Create] AND "European Urology"[Journal] AND "journal article"[Publication Type]) AND (clinicaltrial[Filter] OR randomizedcontrolledtrial[Filter])'

# Execute the query against the API
results = pubmed.query(query, max_results=10000)

with open("European_urology.csv", "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['id', 'title', 'abstract', 'journal', 'mesh', 'keywords', 'date'])
    # Loop over the retrieved articles
    for article in results:
        # Extract and format information from the article
        article_id = article.pubmed_id
        title = article.title
        abstract = article.abstract
        journal = article.journal
        mesh = ";".join(article.mesh)
        keywords = ";".join(article.keywords)
        publication_date = article.publication_date
        csvwriter.writerow([article_id, title, abstract, journal, mesh, keywords, publication_date])
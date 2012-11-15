import csv
from Bio import Entrez
from Bio import Medline
Entrez.email="rvkavu2@uky.edu"

retcount=20000

handle1=Entrez.esearch(db="pubmed", term="(rural health[mh] OR rural health services[mh] OR rural population[mh] OR rural hospital[mh] OR rural development[mh]) AND United States[mh]", retmax=retcount, usehistory="y")
results=Entrez.read(handle1)
handle1.close()
env1=results["WebEnv"]
key1=results["QueryKey"]
medlFormat = Entrez.efetch(db="pubmed", rettype="MEDLINE", retmode="text", retmax=retcount, WebEnv=env1, query_key=key1)
record_list = Medline.parse(medlFormat)
count=0
for rec in record_list:
    if "AB" in rec:
        count = count+1
        g = open("C:\\pubmed\\rural_us2\\"+rec["PMID"]+".txt", 'w')
        g.write(rec["TI"]+"\n"+rec["AB"])
        g.close()
    else:
        count = count+1
        g = open("C:\\pubmed\\rural_us2\\"+rec["PMID"]+".txt", 'w')
        g.write(rec["TI"])
        g.close()        

print count

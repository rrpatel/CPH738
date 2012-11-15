import csv
from Bio import Entrez
from Bio import Medline
Entrez.email="rvkavu2@uky.edu"
import parser

retcount=20000


link = "http://phpartners.org/hp2020/adolescent_health.html"

queryDict, objective, linkToHealthy = parser.getPubMedQuery(link)

for query in queryDict:
    print query
    
    handle1=Entrez.esearch(db="pubmed", term=queryDict[query])
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
                g = open( query +"_"+ rec["PMID"]+".txt", 'w')
                g.write(rec["TI"]+"\n"+rec["AB"])
                g.close()
            else:
                count = count+1
                g = open( query + "_" + rec["PMID"]+".txt", 'w')
                g.write(rec["TI"])
                g.close()        
    
    print count
    break

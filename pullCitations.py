import csv
from Bio import Entrez
from Bio import Medline
Entrez.email="rvkavu2@uky.edu"
import parser

retcount=20000


def execute(link):
    queryDict, objective, linkToHealthy = parser.getPubMedQuery(link)

    counter = 0
    for query in queryDict:


        handle = Entrez.egquery(term=queryDict[query])
        record = Entrez.read(handle)

        tempQ = queryDict[query]
        handle1=Entrez.esearch(db="pubmed", term=tempQ, retmax=retcount, usehistory='y')
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
                    g = open( query +"_" + rec["PMID"] +".txt", 'w')
                    g.write("Title: " + rec["TI"]+"\n"+"Abstract: "+rec["AB"])
                    g.close()
                else:
                    count = count+1
                    g = open( query + "_" + rec["PMID"] + ".txt", 'w')
                    g.write("Title: " + rec["TI"])
                    g.close()
                break
                count += 1
	counter += 1
    print counter


linksToObj = [ "http://phpartners.org/hp2020/adolescent_health.html" , "http://phpartners.org/hp2020/genomics.html" ]

for link in linksToObj:
        execute(link)

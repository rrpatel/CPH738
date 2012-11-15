from bs4 import BeautifulSoup

import urllib


"""
   Function:  processObj(line)  Since line contains unncessary in formation.
	       This method will get rid of unnecessary characters from line.
   Input: Objective in the form of ( AH-* ***** )
   Ouput: AH-1 and Objective separted to be inserted in dictionary by calling function
"""

def processObj(line):
	"""line = line.strip('\w')
	line = line.strip('\t')
	line = line.strip()
	line = line.strip()
	print line """
	line = line.strip()
	tokens = line.split('\n')
	
	##  print tokens[0].strip()        
	
	obj = tokens[0].strip().split()[0]
	
	##  print obj

	objective = ""

	for i in range(1,len(tokens[0].strip().split())):
		objective +=  tokens[0].strip().split()[i]
		if( tokens[0].strip().split()[i] != tokens[0].strip().split()[len(tokens[0].strip().split())-1] ):
			objective += " "
	##  print objective

   ##  return         key                        value

	return tokens[0].strip().split(' ')[0], objective
       


	"""mapObjective = {}
	mapObjective[tokens[0].strip().split(' ')[0]] = objective
	print mapObjective"""
	

"""
   getPubMedQuery(href): Function parses href
   Input: href
   Output: Pubmed Query
"""



def getPubMedQuery(href):
	href = href.replace("http://www.ncbi.nlm.nih.gov/pubmed?term=","")
	href = href.replace("%22",""")
	##  print href
	print "----------------------------------------------------"

	seenParen = 1
	query = "("

	for i in range(1,len(href)):
		if( href[i] == ')' ):
			seenParen -= 1
		elif( href[i] == '(' ):
			seenParen += 1
		if(seenParen!=0):
			query += href[i]
		
	query += ')'

	print query
	return "query"



f = urllib.urlopen("http://phpartners.org/hp2020/adolescent_health.html")
##print f.read()

soup = BeautifulSoup(f) ##  open("http://phpartners.org/hp2020/adolescent_health.html"))

title = ""

for temp in soup.title.text.split():
	title += temp
	if( temp != soup.title.text.split()[len(soup.title.text.split())-1] ):
		title += " "

print title

genObjMap = {}
objectiveMap = {}   ## Map AH-* to corresponding objective
pubmedMap = {}       ## Map AH-* to corresponding pubmed query
healthyMap = {}     ## Map AH-* to corresponding healthy people 2020 (Weblink)



query = ""

nodes = soup.find_all(id="pms")
healthyLink = ""

for node in nodes:
	temp = node.find_all('a')
	##  print "--------------------------------------------------------"

	k, val = processObj(node.text) ##  node.get('href')
	objectiveMap[k] = val

	##  print temp[0].get('href') #len(node) ##  node.get('href')

	pubmedMap[k] = getPubMedQuery(temp[0].get('href'))

	
	##  print "-------------------------------------------------"
	##  print temp[1].get('href')

	healthyLink = temp[1].get('href')
	 
	##  print "--------------------------------------------------------" 

	"""   for entry in objectiveMap:
	print entry + ": " + objectiveMap[entry]   """

genObjMap[title] = healthyLink

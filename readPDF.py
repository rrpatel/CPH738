

##import nltk.data
##from nltk.tokenize import sent_tokenize
import sys

import subprocess


def isObj(tempLine):
	splittedLine = tempLine.split(' ')
	if( tempLine[0] == 'A' and tempLine[1] == 'H' and tempLine[2] == "-" and ( '.' in tempLine or ':' in tempLine)  ):
		return True
	return False


subprocess.call(['pdftotext', 'AdolescentHealth.pdf', 'output'])

f = open('output','r')

tokens = []

for line in f:
	line = line.replace('\n',' ')
	line = line.replace('\t',' ')
	line = line.replace('\r',' ')
	line.replace('\xe2','-')
	temp = line.split(' ')
	for t in temp:
		tokens.append(t)

print len(tokens)

objectives = []

temp = ""
cont = False

for line in f:
	line.rstrip('\t')
	line.rstrip('\r')
	#if line[0] == 'A' and line[1] == 'H':
	tempLine = line.replace('\xe2','-')
	if( isObj(tempLine) or cont ):
		if( isObj(tempLine) ):
			start = 1
			print("Length of line: ")
		else:
			start = 0
		tempLine = tempLine.split(' ')
		cont = True
		##print tempLine
		print(len(tempLine))
		for i in range(start,len(tempLine)): ##word in tempLine: ##x = 1 ##if re.match(r"AH-""+", "a1b2c3")
			##print word
			##if "\n" not in tempLine:
			temp += tempLine[i].rstrip('\n')
			#print 'Newline in line'
			temp += " "
			##print temp
		if "." in line:
			print temp
			cont = False
			objectives.append(temp)
			temp = ""


"""
for j in range(0,len(f)):
	#if line[0] == 'A' and line[1] == 'H':
	f[j] = line.replace('\xe2','-')
	if( isObj(tempLine) or cont ):
		if( isObj(tempLine) ):
			start = 1
		else:
			start = 0
		tempLine = tempLine.split(' ')
		cont = True
		##print tempLine
		for i in range(0,len(tempLine)): ##word in tempLine: ##x = 1 ##if re.match(r"AH-""+", "a1b2c3")
			##print word
			##if "\n" not in tempLine:
			temp += tempLine[i].rstrip('\n')
			#print 'Newline in line'
			temp += " "
			##print temp
		if "." in line:
			##print tempLine
			cont = False
			objectives.append(temp)
			temp = ""


for obj in objectives:
	print obj
	


infile = open('output')
slist = []
for line in infile:
    slist.append(sent_tokenize(line))
print slist
infile.close()"""
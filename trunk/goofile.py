#!/usr/bin/env python
import time
import string
import httplib,sys
from socket import *
import re
import getopt

# TheHarvester used for inspiration
#              
# www.edge-security.com


print "\n-------------------------------------"
print "|Goofile V1.0	                    |"
print "|Coded by Thomas (G13) Richards     |"
print "|www.g13net.com                     |"
print "|code.google.com/p/goofile          |"
print "-------------------------------------\n\n"

global word
global w
global result
result =[]

def usage():
 print "Goofile 1.0\n"
 print "usage: goofile options \n"
 print "       -d: domain to search\n"
 print "       -f: filetype (ex. txt)\n"
 print "example:./goofile.py -d microsoft.com -l 500 -f txt\n" 
 sys.exit()

def run(w,file):
	
	h = httplib.HTTP('www.google.com')
	h.putrequest('GET',"/search?q=site:"+w)
	h.putheader('Host', 'www.google.com')
	h.putheader('User-agent', 'Internet Explorer 6.0 ')
	h.endheaders()
	returncode, returnmsg, headers = h.getreply()
	data=h.getfile().read()
	return data

def test(argv):
	if len(sys.argv) < 1: 
		usage() 
	try :
	       opts, args = getopt.getopt(argv,"d:f:")
 
	except getopt.GetoptError:
  	     	usage()
		sys.exit()
	
	for opt,arg in opts :
    	   	if opt == '-d' :
			word=arg
		elif opt == '-f':
			file=arg
	
	print "Searching in "+word+" for "+ file
	print "========================================"


	print "Searching results: "+"\r"
	res = run(word,file)
	for x in res:
	               if result.count(x) == 0:
               		       result.append(x)
		
			

	print "\nAccounts found:"
	print "====================\n"
	t=0
	if result==[]:
		print "No results were found"
	else:
		for x in result:
			x= re.sub('<li class="first">','',x)
			x= re.sub('</li>','',x)
			print x
			t+=1
	print "====================\n"
	

if __name__ == "__main__":
        try: test(sys.argv[1:])
	except KeyboardInterrupt:
		print "Search interrupted by user.."
	except:
		sys.exit()
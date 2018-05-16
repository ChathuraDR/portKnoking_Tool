#! /usr/bin/python3.5

from itertools import permutations
import sys
import os
import time

ncolr = '\x1b[0m'
colr = '\x1b[6;32m'


ports = sys.argv[1].split(',')
lport = sys.argv[2]

lhost = input("Enter URL/IP to preoceed : ")

perm = []
knocking = "nmap -Pn -sT " + lhost + " -p" 
checking = "nc -vz -w 1 " + lhost + " " + lport

list = permutations(ports)

for n,r in enumerate(list):
	perm.append([])
	for m,c in enumerate(r):
		perm[n].append(c)

##################################################
################# Let's Knock ####################
##################################################


for row in perm:
	print ("\n###########################################################################\n")
	print ( colr + "Combination : " + str(row) + ncolr )
	print ("---------------------------------------------------------------------------")
	for p in row:
		os.system(knocking+p)
		print ("---------------------------------------------------------------------------")
		time.sleep(1)
			
	os.system(checking)
	if(input("Do you want to continue [y/n]?") == "n"):
		break	

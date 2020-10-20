#!/usr/bin/env python3

import sys


pdbname=sys.argv[1]

f = open(pdbname, 'r')
lines = f.readlines()

list = []

for l in lines:

  words = l.split()
  list.append(words) 

print(list) 
f.close()
print("Done!")

#***********************************
fout= open("NewpdbFile.pdb",'w')
for words in lines:
	fout.write(words)
fout.close()

#!/usr/local/bin/python3
#https://github.com/hk19j/bch5884.git

import sys, math

############################# Reading PDBs #############################
def pdbread(filename):
  F=open(filename, 'r')
  return F.readlines()
  F.close()

##############################  Parsing PDBs ##############################

def parsing(PDB):
  atoms=[]
  for line in PDB:
    if line[0:4]=="ATOM":
      recordname=line[0:6]
      atomnumber=int(line[6:11])
      atomname=line[12:16]
      resName=line[17:20]
      chainid=line[21:22]
      resSeq=int(line[23:26])
      null=line[26:30]
      X=float(line[30:38])
      Y=float(line[38:46])
      Z=float(line[46:54])
      occupency=float(line[54:60])
      tempfact=float(line[60:66])
      null2=line[66:76]
      element=line[76:78]
      atoms.append(line)
  return atoms


###################### Calculate RMSD for two parsed PDBs ######################


def rmsdcalc(pdb1,pdb2):
	SUM1=0
	for i in range(len(pdb1)):
		vx=float(pdb1[i].split()[6])
		wx=float(pdb2[i].split()[6])
		vy=float(pdb1[i].split()[7])
		wy=float(pdb2[i].split()[7])
		vz=float(pdb1[i].split()[8])
		wz=float(pdb2[i].split()[8])
		X1=(vx-wx)**2
		Y1=(vy-wy)**2
		Z1=(vz-wz)**2
		SUM1=SUM1+X1+Y1+Z1
	RMSD= math.sqrt(SUM1/len(pdb1))
	return RMSD
	

################################### Execute ###################################

pdbfile1= pdbread('2FA9noend.pdb')
pdbfile2= pdbread('2FA9noend2mov.pdb')

RMSD_value= rmsdcalc(pdbfile1,pdbfile2)

print ("RMSD:" ,RMSD_value)
import os, sys
import fileinput
import re

def executeCMD(command):
	print("Executing: ", command)
	os.system(command)


fitDir = sys.argv[1]
#fitName = fitDir.split("/")[-1]
fitName = sys.argv[2]

if("NAL" in fitDir):
	cp_had_workspaces = "cp {0}/NAL*/base*root {1}/hadronic_workspaces/.".format(fitDir,fitName)
else:
	cp_had_workspaces = "cp {0}/??/base*root {1}/hadronic_workspaces/.".format(fitDir,fitName)#LL/TT

mkdir 		= "mkdir -p {0}/hadronic_workspaces".format(fitName)
cp_CR_cards = "cp {0}/CR_*txt CR_datacards/.".format(fitDir)
cp_card 		  = "cp {0}/combinedCard.txt {1}/card_{1}.txt".format(fitDir,fitName)
backup_card 	  = "cp {0}/card_{0}.txt {0}/card_{0}_backup.txt".format(fitName)
	
executeCMD(mkdir)
executeCMD(cp_had_workspaces)
executeCMD(cp_CR_cards)
executeCMD(cp_card)
executeCMD(backup_card)


with open('{0}/card_{0}.txt'.format(fitName), 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('/afs/cern.ch/work/m/mrogulji/UL_X_YH/X_YH_4b/results/templates_semileptonic/combined/', '../CR_templates/')
if("NAL" in fitDir):
	filedata = re.sub("\sNAL_./base"," hadronic_workspaces/base",filedata)
else:
	print("Doing this")
	filedata = re.sub("LL/base"," hadronic_workspaces/base",filedata)
	filedata = re.sub("TT/base"," hadronic_workspaces/base",filedata)
# Write the file out again
with open('{0}/card_{0}.txt'.format(fitName), 'w') as file:
  file.write(filedata)
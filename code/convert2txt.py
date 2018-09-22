import os, sys

jobID = sys.argv[1]
query = '_'.join(sys.argv[2:])
foldername = 'Raw_Data/'+str(jobID)+'_'+query

os.system('cd ' + foldername)

os.system

cmd='for var in *.pdf; do pdf2txt.py "$var" > "$var".txt;done'

os.system(cmd)

os.system('cd ..; cd ..; done')
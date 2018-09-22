import os
import sys

jobID = sys.argv[1]
query = '_'.join(sys.argv[2:])
foldername = 'Raw_Data/'+str(jobID)+'_'+query
cmd = 'mkdir '+foldername
os.system(cmd)



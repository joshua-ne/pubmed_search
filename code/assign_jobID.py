
import os

filename = 'Raw_Data/JobID.txt'

with open(filename,'r') as f:
	current = f.readlines()[-1]

nextnum = int(current)+1

with open(filename,'a') as f:
	f.write(str(nextnum)+'\n')

print(nextnum)
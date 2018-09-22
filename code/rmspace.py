import os, sys

if __name__ == '__main__':
	# in test run, len(sys.argv)==1, then use 13 as the jobID and 'cGAS AND STING' as the query
	if len(sys.argv)==1:
		jobID='13'
	else:
		jobID = sys.argv[1]

	foldername = 'Raw_Data/'+str(sys.argv[1])+'_'+'_'.join(sys.argv[2:])
	filename = foldername +'/'+jobID+ '_' +'pubmedID.txt'

	with open (os.path.join(foldername,jobID+'data_sents_rmspace.txt'),'w') as output:
		with open(os.path.join(foldername,jobID+'data_sents.txt'), 'r') as f:
			for line in f:
				if line != '\n':
					output.write(line)
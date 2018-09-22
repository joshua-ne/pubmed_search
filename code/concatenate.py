import os, sys

if __name__ == '__main__':
	# in test run, len(sys.argv)==1, then use 13 as the jobID and 'cGAS AND STING' as the query
	if len(sys.argv)==1:
		jobID='13'
	else:
		jobID = sys.argv[1]

	foldername = 'Raw_Data/'+str(sys.argv[1])+'_'+'_'.join(sys.argv[2:])
	filename = foldername +'/'+jobID+ '_' +'pubmedID.txt'
	
	id_list=[]
	with open(filename,'r') as f:
		for line in f:
			id_list.append(line[:-1])


	with open(os.path.join(foldername,jobID+'data.txt'),'w') as mergedfile:
		for i in id_list:
			with open(os.path.join(foldername,i+'.txt'),'r') as f:
				for line in f:
					mergedfile.write(line)
				mergedfile.write('\n')
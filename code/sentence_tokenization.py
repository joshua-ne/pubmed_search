import os,spacy,sys
#os.environ["https_proxy"] = "proxy.swmed.edu:3128"


if __name__ == '__main__':
	# in test run, len(sys.argv)==1, then use 13 as the jobID and 'cGAS AND STING' as the query
	if len(sys.argv)==1:
		jobID='13'
	else:
		jobID = sys.argv[1]

	en_nlp = spacy.load('en')
	foldername = 'Raw_Data/'+str(sys.argv[1])+'_'+'_'.join(sys.argv[2:])
	filename = foldername +'/'+jobID+ '_' +'pubmedID.txt'

	with open(os.path.join(foldername,jobID+'data_sents.txt'),'w') as output:

		with open(os.path.join(foldername,jobID+'data.txt'),'r') as f:
			for line in f:
				en_doc = en_nlp(line)

				for sent in en_doc.sents:
					output.write(str(sent))
					output.write('\n')

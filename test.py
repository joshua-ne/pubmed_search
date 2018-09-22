import os,spacy
#os.environ["https_proxy"] = "proxy.swmed.edu:3128"


if __name__ == '__main__':

	en_nlp = spacy.load('en')
	#foldername = 'Raw_Data/'+str(sys.argv[1])+'_'+'_'.join(sys.argv[2:])
	#filename = foldername +'/'+jobID+ '_' +'pubmedID.txt'

	with open(('data_sents.txt'),'w') as output:

		with open(('test.txt'),'r') as f:
			for line in f:
				en_doc = en_nlp(line)

				for sent in en_doc.sents:
					output.write(str(sent))
					output.write('\n')

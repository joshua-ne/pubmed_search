from Bio import Entrez
import os, sys
#os.environ["https_proxy"] = "proxy.swmed.edu:3128"

def search(query):
	Entrez.email='renjunyao@gmail.com'
	handle = Entrez.esearch(db='pubmed', 
                            sort='relevance', 
                            retmax='5',
                            retmode='xml', 
                            term=query)
	results = Entrez.read(handle)
	return results

if __name__ == '__main__':
	# in test run, len(sys.argv)==1, then use 13 as the jobID and 'cGAS AND STING' as the query
	if len(sys.argv)==1:
		jobID = '13'
		results = search('cGAS AND STING')
	else:
		jobID = sys.argv[1]
		query = ' '.join(sys.argv[2:])
		results = search(query)
    
	foldername = 'Raw_Data/'+str(sys.argv[1])+'_'+'_'.join(sys.argv[2:])

	id_list = results['IdList']

	filename = foldername +'/'+jobID+ '_' +'pubmedID.txt'

	print('Retrieving PubMed IDs of publication with query "' + query + '" ')

	with open(filename, 'w') as f:
		for id in id_list:
			f.write(id)
			f.write('\n')

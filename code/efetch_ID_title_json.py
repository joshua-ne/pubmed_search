from Bio import Entrez
import os, sys, json
#os.environ["https_proxy"] = "proxy.swmed.edu:3128"

def fetch_details(sid):
	Entrez.email = 'renjunyao@example.com'
	handle = Entrez.efetch(db='pubmed',
							retmode='xml',
							id=sid)
	results = Entrez.read(handle)
	return results

# get url from a given fetched details of a paper
def geturl(record):

	url = 'Currently the full-text not available'
	if record.get('MedlineCitation'):
			if record['MedlineCitation'].get('OtherID'):
				for other_id in record['MedlineCitation']['OtherID']:
					if other_id.title().startswith('Pmc'):
						url='http://www.ncbi.nlm.nih.gov/pmc/articles/%s/pdf/' % (other_id.title().upper())
	return url



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

	print (id_list)

	metadata={}

	for sid in id_list:
		try:
			result = fetch_details(sid)
			paper=result["PubmedArticle"][0]
			filename= foldername +'/'+sid+'_ID_title.txt'
			with open(filename, 'w') as f:
				#paperurl=geturl(paper)
				#f.write(paperurl+' ')

				articleinfo = paper['MedlineCitation'].get('Article')
				f.write(str(articleinfo.get('ArticleTitle'))+' ')
				f.write(sid+' ')
				metadata[sid] = str(articleinfo.get('ArticleTitle'))
				f.write(str(articleinfo.get('Journal').get('Title'))+' ')
				f.write(str(articleinfo.get('Abstract').get('AbstractText'))+' ')

				#if 'available' not in paperurl:
					#wgetcommand = 'wget --user-agent="chrome" -O ' + foldername + '/' + sid + '.pdf ' + paperurl
					#os.system(wgetcommand)
					#pass
		except:
			pass

	with open(os.path.join(foldername,jobID+'metadata.json'), 'w') as fp:
		json.dump(metadata, fp)


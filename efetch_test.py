from Bio import Entrez
import os, sys, json
#os.environ["https_proxy"] = "proxy.swmed.edu:3128"

sid = '28334992'
Entrez.email = 'renjunyao@example.com'
handle = Entrez.efetch(db='pubmed',
     	              retmode='xml',
     	              id=sid)
results = Entrez.read(handle)

print((results))
for result in results:
	print(result)
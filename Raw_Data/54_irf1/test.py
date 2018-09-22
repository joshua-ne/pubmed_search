import os

foldername = '~/Desktop/pubmed/Raw_Data/54_irf1'

i = '25347735'

cmd = 'rm ' + os.path.join(foldername,i+'_ID_title.txt')
os.system('cmd')
#!/bin/sh

echo '\n'
echo 'Initalization started...\n'

echo 'Assigning jobID...\n'
# Assuming the jobID is 13 for now

jobID=$(python3 code/assign_jobID.py)

echo 'Your JobID is: '$jobID "\n"

echo 'Initalization finished successfully!'

read -p "Input your query:" query

python3 code/create_folder.py $jobID $query

python3 code/retrieve_ID_list.py $jobID $query

echo 'ID list successfully retrieved, now trying to retrieve detail for each paper and download full-text if available...'

#python code/efetch_ID_title.py $jobID $query

python3 code/efetch_ID_title_json.py $jobID $query

python3 code/efetch_detail.py $jobID $query

##echo 'converting pdf files to txt files'

##foldername=$(python code/get_folder_name.py $jobID $query)

##echo $foldername
##cd "$foldername"

##pwd

##for var in *.pdf; do pdf2txt.py "$var" > "$var".txt;done

##Concatenate abstracts
python3 code/concatenate.py $jobID $query

python3 code/concatenate_ID_title.py $jobID $query

python3 code/sentence_tokenization.py $jobID $query

python3 code/rmspace.py $jobID $query


echo 'done'

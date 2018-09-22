import os

os.environ["https_proxy"] = "proxy.swmed.edu:3128"


cmd='python -m spacy.en.download all'

os.system(cmd)
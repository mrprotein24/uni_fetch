#!/usr/bin/python
import csv
import sys
import time
import os

import requests


#optional step to keep a track of time
#start_time = time.clock()

#Put file path
with open("xxx/list_uniprotIDs.csv", "r") as infile:



#parse
if len(sys.argv) < 2 or len(sys.argv) > 3:
    print("input and output paths need to be defined.")
    print("Run the code as: python code.py list_uniprotIDs.csv /xxx/output.fasta")
    sys.exit()

prot_list = sys.argv[1]


if len(sys.argv) == 3:
    output = sys.argv[2] #output location    
else:
    output = os.getcwd() #default output stored in current dir



#meat of the code

with open(prot_list, "r") as infile:
    readx = csv.reader(infile)
    next(readx, None)
    for linex in readx:
        ID = linex[0]
        url = 'http://www.uniprot.org/uniprot/' + ID +'.fasta'
        print("Downloading information: ", url)
        
        response = requests.get(url)
        
        putoutput_location = output + "\\" + ID + '.fasta'
        
        with open(putoutput_location, 'wb') as f:
            f.write(response.content)


#optional line to compute run time
#print("---%s seconds---" % (time.clock() - start_time))

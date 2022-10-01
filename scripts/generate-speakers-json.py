#! /usr/bin/env python3
import csv
import sys
import json
import os

if len(sys.argv) != 2:
    raise Exception(f"Missing csv file as argument. Use: {sys.argv[0]} <csv file> ")
CSVFile = sys.argv[1]

if not os.path.exists(CSVFile):
    raise Exception(f"File \"{CSVFile}\" not found")

with open(CSVFile) as csvfile:
    csvreader = csv.DictReader(csvfile)
    speakers = []
    for row in csvreader:
        status = row["status"] 
        if status != "Accepted": 
            continue 
        speakers.append({
        "cfp_type" : row["cfp_type"],
        "title" : row["title"],
        "author" : row["author"],	
        #email	
        "others" : row["others"],	
        "abstract" : row["abstract"],
        #notes	
        "bio" : row["bio"],	
        "level" : row["level"],
        "twitter" : row["twitter"],
        "linkedin" : row["linkedin"],
        "instagram" : row["instagram"] 
        })

print(json.dumps(speakers, indent=4))
    

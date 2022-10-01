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
        data = {}
        data["cfp_type"] = row["cfp_type"]
        data["title"] = row["title"]
        data["author"] = row["author"]	
        #email	
        data["others"] = row["others"]
        data["abstract"] = row["abstract"]
        #notes	
        if row["bio"]: 
            data["bio"] = row["bio"]
        data["level"] = row["level"]
        if row["twitter"]: 
            data["twitter"] = row["twitter"]
        if row["linkedin"]: 
            data["linkedin"] = row["linkedin"]
        if row["instagram"]:
            data["instagram"] = row["instagram"]
        if row["picture"]: 
            data["picture"] = row["picture"]
        speakers.append(data)

print(json.dumps(speakers, indent=4))
    

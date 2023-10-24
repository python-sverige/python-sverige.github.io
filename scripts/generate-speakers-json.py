#! /usr/bin/env python3
import csv
import sys
import json
import os

if len(sys.argv) != 2:
    raise Exception(
        f"Missing csv file as argument. Use: {sys.argv[0]} <csv file> ")
CSVFile = sys.argv[1]

if not os.path.exists(CSVFile):
    raise Exception(f"File \"{CSVFile}\" not found")

with open(CSVFile) as csvfile:
    csvreader = csv.DictReader(csvfile)
    speakers = []
    for row in csvreader:
        status = row["Confirmed"]
        if status.lower() != "yes":
            continue
        data = {}
        # avoiding personal data like email
        if row["Talk/Workshop title"] == "":
            continue
        for row_name in [
                "Twitter", "Linkedin", "Instagram", "Mastodon", "Images",
                "Your biography", "Audience knowledge level", "Abstract",
                "Proposal type", "Talk/Workshop title", "Your name"
        ]:
            if not row_name in row:
                continue
            if row[row_name] and row[row_name] is not None:
                data[row_name] = row[row_name]
        speakers.append(data)

print(json.dumps(speakers, indent=4))

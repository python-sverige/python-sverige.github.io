#! /usr/bin/env python3
import csv
import sys
import json
import os
import argparse

parse = argparse.ArgumentParser(description="Script to generate speakers json file")
parse.add_argument("--csvfile", required=True, help="The CSV file exported with speakers information")
args = parse.parse_args()

CSVFile = args.csvfile

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

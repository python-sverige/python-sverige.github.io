#! /usr/bin/env python3
import os
import argparse
import json
import shutil
import requests

class PretixSpeakerParser:
    def __init__(self):
        parse = argparse.ArgumentParser(description="Parse the Pretix's json from speakers and fetch the pictures")
        parse.add_argument("--jsonspeakers", required=True, help="The json file exported from Pretix for speakers")
        parse.add_argument("--jsonsessions", required=True, help="The json file exported from Pretix for sessions")
        args = parse.parse_args()

        self.speakersData = self.parseJSON(args.jsonspeakers)
        self.sessionsData = self.parseJSON(args.jsonsessions)
        self.setSessionByID()
        self.speakersJSON = []

    def parseJSON(self, filename):
        with open(filename) as fh:
            data =  json.load(fh)
        return data

    def setSessionByID(self):
        sessionByID = {}
        for session in self.sessionsData:
            """
            {
                "ID": <Proposal ID>,
                "Proposal title": <title>,
                "Session type": {
                    "en": <Talk|Workshop|Keynote>
                },
                "Abstract": <abstract>,
                "Description": <description>,
               "Speaker IDs": [
                   <Speaker ID>
               ],
               "Speaker names": [
                   <Name>
               ]
            }
            """
            if len(session["Speaker IDs"]) == 0:
                print("Skipping reference for:", session["Proposal title"])
                continue
            for i in session["Speaker IDs"]:
                sessionByID[i] = {
                    "Title": session["Proposal title"],
                    "Type": session["Session type"]["en"],
                    "Abstract": session["Abstract"],
                    "Description": session["Description"]
                }

        self.sessionsData = sessionByID

    def parseSpeakers(self):
        for speaker in self.speakersData:
            """
            {
                "ID": "<random ID - matching the talk>",
                "Name": "<First and Last name>",
                "Email": "<email>",
                "Picture": "<url for the image>",
                "Biography": <biography",
                "Proposal IDs": [ ],
                "Proposal titles": [ ]
            },
            """
            author = speaker["Name"]
            print(f"Getting image path for: {author}")
            meta_name = "_".join(author.split())
            _, extension = os.path.splitext(speaker["Picture"])

            img_filename = meta_name + extension.lower()
            session = self.sessionsData[speaker["ID"]]
            self.speakersJSON.append(
                {
                    "Image": "images/speakers/" + img_filename,
                    "Biography": speaker["Biography"],
                    "Title": session["Title"],
                    "Type": session["Type"],
                    "Abstract": session["Abstract"],
                    "Description": session["Description"],
                    "Name": speaker["Name"]
                }
            )

    def generateJSON(self):
        result = json.dumps(self.speakersJSON, indent=4)
        with open("speakers.json", "w") as fh:
            print(result)
            fh.write(result)

if __name__ == '__main__':
    data = PretixSpeakerParser()
    data.parseSpeakers()
    data.generateJSON()

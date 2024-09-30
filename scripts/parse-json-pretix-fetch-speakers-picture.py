#! /usr/bin/env python3
import os
import argparse
import json
import shutil
import requests

from PIL import Image

class PretixSpeakerParser:
    def __init__(self):
        parse = argparse.ArgumentParser(description="Parse the Pretix's json from speakers and fetch the pictures")
        parse.add_argument("--jsonfile", required=True, help="The json file exported from Pretix")
        args = parse.parse_args()
        self.args = args

        self.parseJSON()

    def parseJSON(self):
        with open(self.args.jsonfile) as fh:
            self.data =  json.load(fh)


    def fetchAll(self):
        for speaker in self.data:
            """
            {
                "ID": "<random ID - matching the talk>",
                "Name": "<First and Last name>",
                "Email": "<email>",
                "Picture": "<url for the image>"
            },
            """
            author = speaker["Name"]
            print(f"Fetching image for: {author}")
            meta_name = "_".join(author.split())
            _, extension = os.path.splitext(speaker["Picture"])

            temp_filename = meta_name + "-orig" + extension.lower()
            final_filename = meta_name + extension.lower()

            if self.downloadPicture(speaker["Picture"], temp_filename):
                print(f'Downloaded image for {speaker["Name"]}: {temp_filename}')
            else:
                print(f'Failed to download image for {speaker["Name"]}: url={speaker["Picture"]}')
                continue
            self.resizePicture(temp_filename, final_filename)
            
    def downloadPicture(self, url: str, destination: str) -> bool:
        try:
            req = requests.get(url, stream=True)
        except requests.exceptions.MissingSchema:
            print("Failed to parse url:", url)
            return False
        if req.status_code != 200:
            print(f"Not good status code: {url} (code: {req.status_code})")
            return False
        with open(destination, 'wb') as fh:
            for chunk in req:
                fh.write(chunk)
        return True

    def resizePicture(self, original: str, destination: str) -> bool:
        print(f"Resizing: {original}")
        # resize to 400x400 or alike
        base_width = 400
        img = Image.open(original)
        wpercent = (base_width / float(img.size[0]))
        hsize = int(float(img.size[1]) * float(wpercent))
        img = img.resize((base_width, hsize), Image.Resampling.LANCZOS)
        img_rgb = img.convert('RGB')
        try:
            img_rgb.save(destination)
        except OSError as e:
            print("Failed to generate: {destination}:", e)
        print(f"Created: {destination}")
        return True





if __name__ == '__main__':
    speakers = PretixSpeakerParser()
    speakers.fetchAll()

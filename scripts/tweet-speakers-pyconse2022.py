#! /usr/bin/env python3

import configparser
import csv
import os
import twitter
import argparse
import sys

# to generate your twitter credentials, use the script from here:
# https://raw.githubusercontent.com/bear/python-twitter/master/get_access_token.py
# consumer_key and consumer_secret, ping me (Helio)
# save the data into ~/.twitterc under section [PYCONSE]

HOME = os.environ.get('HOME')

# the block below is just to find the images properly
PROGRAM = sys.argv[0]
PROGRAMDIR = os.path.dirname(PROGRAM)
CURDIR = os.path.abspath(PROGRAMDIR)
ROOTDIR = os.path.abspath(CURDIR + '/..')
print(f"current directory: {CURDIR}")
print(f"root dir: {ROOTDIR}")

cfg = configparser.ConfigParser()
cfg.read(f"{HOME}/.twitterc")

consumer_key         = cfg.get("PYCONSE", "consumer_key")
consumer_secret      = cfg.get("PYCONSE", "consumer_secret")
access_token_key     = cfg.get("PYCONSE", "access_token_key")
access_token_secret  = cfg.get("PYCONSE", "access_token_secret")

api = twitter.Api(
    consumer_key=consumer_key, 
    consumer_secret=consumer_secret,
    access_token_key=access_token_key, 
    access_token_secret=access_token_secret,
    input_encoding="utf-8")

#api.PostUpdate("PyCon Sweden is coming...")

parser = argparse.ArgumentParser(description="It sends tweets regarding speakers.")
parser.add_argument("--csv", help="CSV file with speakers list")
args = parser.parse_args()

if args.csv is None:
    raise Exception("Missing csv file to read content.")

def generateTwitter(line):
    # split line on "/"s and get the last text at the end
    twitter = line.split("/")[-1]
    return '@' + twitter

with open(args.csv, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # skip if not accepted
        if row['status'] != "Accepted":
            continue
        # skip if missing canva card
        if row['card'] is None:
            continue
        card = ROOTDIR + '/' + row['card']
        hasTwitterFlag = False
        twitter = row['twitter']
        tw_speakers = []
        if twitter:
            hasTwitterFlag = True
            tw_speakers = twitter.split()
        author = row['author']
        title = row['title']
        cfp_type = row['cfp_type']
        #print(f"{author} twitter status is {hasTwitterFlag} and card is {card}")
        if hasTwitterFlag:
            tw_ats = []
            for person in tw_speakers:
                tw_ats.append(generateTwitter(person))
            author = " and ".join(tw_ats)

        if not os.path.exists(card):
            raise Exception(f"File {card} couldn't be found in order to send to Twitter.")
        text = f"{author} will be presenting {cfp_type} \"{title}\" at PyCon Sweden 2022.\n#pyconse2022\n#pyconse"
        print(text)
        api.PostUpdate(text, media=card)


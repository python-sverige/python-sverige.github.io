#! /usr/bin/python3

import csv
import sys
import os
import re
import argparse

def usage(errcode=0) -> None:
    print(f"Use: {sys.argv[0]} <csv file>")
    print("  Download the csv file from gdrive.  The schedule and video links.")
    print("  Just select to download as csv.")
    sys.exit(errcode)

def mailCompose(dataDic) -> str:
    """
    Just returns a mail composed.
    """
    email = dataDic["email"]
    author = dataDic["author"]
    title = dataDic["title"]
    date = dataDic["date"]
    start = dataDic["start"]
    youtube = dataDic["youtube"]
    streamyard = dataDic["streamyard"]

    return f"""To: {email}
Subject: Your access to PyCon Sweden video session
Hi {author},

Your talk: {title}.
Date: {date}.
Time: {start} (CET).

You access during your talk (don't share): {streamyard}

Your stream on YouTube: {youtube}

PyCon Sweden organization
"""

def parse():
    """
    It parses a certain CSV file (expected to be
    the first argument) and returns a dict.
    """
    parser = argparse.ArgumentParser(description='Generates email format to inform streamyard and youtube link.')
    parser.add_argument('--track', dest='track',
                    help='an integer for the accumulator')
    parser.add_argument('csvfile', type=str,
                        help="a csv file downloaded from gsuite")

    args = parser.parse_args()
    print("track:", args.track)
    print("csvfile:", args.csvfile)

    if not os.path.exists(args.csvfile):
        parser.print_help()
        sys.exit(os.EX_NOINPUT)

    def generateDict(author, title, date, start, email, youtube, streamyard):
        return {
            "author" : author,
            "title" : title,
            "date" : date,
            "start" : start,
            "email" : email,
            "youtube" : youtube,
            "streamyard" : streamyard }

    authorData = {}
    with open(args.csvfile, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            track = row['track']
            if track != args.track:
                continue
            date = row["date"]
            start = row["start"]
            title = row["title" ]
            author = row['author']
            email = row['email']
            youtube = row['Youtube']
            streamyard = row['StreamYard']
            if re.search("\n", author):
                authors =  author.splitlines()
                emails = email.splitlines()
                for i in range(len(authors)):
                    authorData[authors[i] + title + date] = generateDict(authors[i],
                                                                         title,
                                                                         date,
                                                                         start,
                                                                         emails[i],
                                                                         youtube,
                                                                         streamyard)
                    print(authors[i], emails[i], "added")
            else:
                authorData[author + title + date] = generateDict(author,
                                                  title,
                                                  date,
                                                  start,
                                                  email,
                                                  youtube,
                                                  streamyard)
                print(row['author'], row['email'], "added")
    return authorData


def generate(dataDic):
    """
    It generates output per author w/ information regarding youtube link and streamyard.
    """
    for entry in dataDic.keys():
        mailContent = mailCompose(dataDic[entry])
        print(80 * "=")
        print(mailContent)
        print(80 * "=")

if __name__ == '__main__':
    data = parse()
    generate(data)

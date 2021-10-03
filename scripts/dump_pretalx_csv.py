#! /usr/bin/python3

import requests, json, os, sys, re
import csv


URL="https://pretalx.com/pycon-sweden-2021/schedule/export/schedule.json"
URLAUTHORS="https://pretalx.com/api/events/pycon-sweden-2021/speakers/?format=json&limit=120"


def debug(*msg):
    if os.environ.get("DEBUG"):
        print(*msg)

def curl(url):
    authorization_token = os.environ.get("PRETALX_TOKEN")
    if authorization_token is None:
        raise Exception("Missing pretalx's authorization token on environment variable PRETALX_TOKEN.")

    headers = { "Authorization" : f"Token {authorization_token}"}

    req = requests.get(url, headers=headers)

    if req.status_code != 200:
        raise Exception("Failed to fetch schedule:", req.status_code)
    return req.text

jSchedule = json.loads(curl(URL))
debug(json.dumps(jSchedule, indent=4))
jAuthors = json.loads(curl(URLAUTHORS))
debug(json.dumps(jAuthors, indent=4))

author_map = {}
for author_data in jAuthors["results"]:
    email = author_data["email"]
    name = author_data["name"]
    author_map[name] = email

with open("pycon-sweden-2021.csv", "w", newline='') as csvfile:
    fieldnames = [ "date", "start", "duration", "track", "title", "author", "email" ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for day in jSchedule["schedule"]["conference"]["days"]:
        debug("Day:", day)
        for room in day["rooms"]:
            debug(" * room:", room)
            for talk in day["rooms"][room]:
                debug(" * * talk:", talk)
                title = talk["title"]
                abstract = talk["abstract"]
                description = talk["description"]
                authors = talk["persons"]
                date = talk["date"]
                date = re.sub("T.*", "", date)
                start = talk["start"]
                duration = talk["duration"]
                track = talk["room"]

                author = ""
                if len(authors) == 1:
                    author = authors[0]["public_name"]
                    try:
                        email = author_map[author]
                    except KeyError:
                        email = "none"

                else:
                    authors_group = []
                    emails = []
                    for identity in authors:
                        this_author = identity["public_name"]
                        authors_group.append(this_author)
                        try:
                            emails.append(author_map[this_author])
                        except KeyError:
                            emails.append("none")
                    author = " and ".join(authors_group)
                    email = " and ".join(emails)
                line = f"{date},{start},{duration},{track},{title},{author},{email}"
                debug(line)
                writer.writerow({
                    "date": date,
                    "start" : start,
                    "duration" : duration,
                    "track" : track,
                    "title" : title,
                    "author" : author,
                    "email" : email
                })






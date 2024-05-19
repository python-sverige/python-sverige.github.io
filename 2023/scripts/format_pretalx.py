#! /usr/bin/python3

import requests, json, os
import datetime
import sys

URL="https://pretalx.com/pycon-sweden-2021/schedule/export/schedule.json"

if len(sys.argv) != 2:
    print("Usage: %s [Track]" % sys.argv[0])
    exit(1)

room_responsible = sys.argv[1]

authorization_token = os.environ.get("PRETALX_TOKEN")
if authorization_token is None:
    raise Exception("Missing pretalx's authorization token on environment variable PRETALX_TOKEN.")

headers = { "Authorization" : f"Token {authorization_token}"}

req = requests.get(URL, headers=headers)

if req.status_code != 200:
    raise Exception("Failed to fetch schedule:", req.status_code)

jSchedule = json.loads(req.text)
#print(json.dumps(jSchedule, indent=4))

for day in jSchedule["schedule"]["conference"]["days"]:
    #print("Day:", day)
    for room in day["rooms"]:
        #print(" * room:", room)
        for talk in day["rooms"][room]:
            if talk["room"] == room_responsible:
                #print(" * * talk:", talk)
                title = talk["title"]
                session_type = talk["type"]
                abstract = talk["abstract"].replace("\n\r", " ").replace("\n", " ").replace("\r", " ")
                #description = talk["description"]
                authors = talk["persons"]
                date = talk["date"]
                room_name = talk["room"]
                url = talk["url"]
                if day["date"] == "2021-10-21":
                    scheduled_day = "Day 1"
                elif day["date"] == "2021-10-22":
                    scheduled_day = "Day 2"
                else:
                    raise Exception("Wrong date "+day["date"])

                if session_type is not "Keynote" and session_type is not "Workshop" and session_type is not "Panel":
                    print(f"{session_type} ({room_name} - {scheduled_day}) - {title}\n")
                else:
                    print(f"{session_type} ({scheduled_day}) - {title}\n")
                print(f"Abstract: {abstract}\n")
                #print(f"Description: {description}\n")
                print(f"For more details: {url}\n")
                if len(authors) == 1:
                      author = authors[0]["public_name"]
                      bio = authors[0]["biography"]
                      #print(f"Speaker: {author}. {bio}")
                      print(f"Speaker: {author}")
                else:
                    print("Speakers:")
                    for identity in authors:
                      author = identity["public_name"]
                      bio = identity["biography"]
                      #print(f"\t{author}.  {bio}")
                      print(f"\t{author}")
                print("=" * 80)





#! /usr/bin/python3

import requests, json, os


URL="https://pretalx.com/pycon-sweden-2021/schedule/export/schedule.json"


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
            #print(" * * talk:", talk)
            title = talk["title"]
            abstract = talk["abstract"]
            description = talk["description"]
            authors = talk["persons"]
            date = talk["date"]

            print(f"Title: {title}\n")
            print(f"Abstract: {abstract}\n")
            print(f"Description: {description}\n")
            if len(authors) == 1:
                  author = authors[0]["public_name"]
                  bio = authors[0]["biography"]
                  print(f"Author: {author}.  {bio}")
            else:
                print("Authors:")
                for identity in authors:
                  author = identity["public_name"]
                  bio = identity["biography"]
                  print(f"\t{author}.  {bio}")
            print("=" * 80)





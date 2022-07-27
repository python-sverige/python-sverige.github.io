#! /usr/bin/env python3

import argparse
import json
import sys
import os


BOARDFILE = "board.json"

def readJson():
    with open(BOARDFILE) as stream:
        j = json.load(stream)
    return j

def saveJson(data):
    with open(BOARDFILE, 'w') as stream:
        stream.write(json.dumps(data, indent=4))

def checkExists(fullName, data):
    for entry in data['members']:
        if entry['name'] == fullName:
            return True
    return False

def addMember(member):
    data = readJson() 
    memberName, memberTitle, memberPhoto, memberTwitter, memberGithub, memberFacebook = member.split(',')
    if checkExists(memberName, data):
       print(f'ERROR: {memberName} already exists.')
       sys.exit(os.EX_CONFIG)
    memberData = {
        'name': memberName,
        'title': memberTitle
    }
    if memberPhoto != "none":
        memberData['photo'] = memberPhoto
    if memberFacebook != "none":
        memberData['facebook'] = memberFacebook
    if memberGithub != "none":
        memberData['github'] = memberGithub
    if memberTwitter != 'none':
        memberData['twitter'] = memberTwitter
    data['members'].append(memberData)
    saveJson(data)


def delMember(memberName):
    data = readJson()
    if not checkExists(memberName, data):
        print(f'ERROR: {memberName} not found in the json file')
        sys.exit(os.EX_CONFIG)
    keepData = []
    for entry in data['members']:
        if not entry['name'] == memberName:
            keepData.append(entry)
    data['members'] = keepData
    saveJson(data)
   

parse = argparse.ArgumentParser(description="Add or delete members from board.json file")
parse.add_argument('--add', help='Add a member.  Format: <full name>,<title>,<photo>,<twitter>,<github>,<facebook>.  Use "none" for null values.')
parse.add_argument('--remove', help='Remove a member. Format: <full name>')
parse.add_argument('--update', help='Update a member entry.  Format:<full name>,<title>,<photo>')
args = parse.parse_args()

if args.add is not None:
    addMember(args.add)
elif args.remove is not None:
    delMember(args.remove)
elif args.update is not None:
    updateMember(args.update)
else:
    print('Uknown option selected')
    parse.print_help()

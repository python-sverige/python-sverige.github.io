#! /usr/bin/env python3
# src: https://scriptreference.com/sending-emails-via-gmail-with-python/
import pickle
import os
import base64
import googleapiclient.discovery
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv
import sys
import argparse
import json


def sendMail(pretix, pretalx, contactdata, dryrun, service):
    # Create a message
    # Name,Role,Voucher,Link,Send,Redeem,,Name,Role,Voucher,Link
    my_email = 'info@pycon.se'
    author = pretalx['Name']
    email = pretalx['Email']
    promocode = pretix['Voucher']
    promolink = pretix['Link']
    for address in [email]:
        if address == "":
            continue
        print(f"Address: {author}<{email}>")
        msg = MIMEMultipart('alternative')
        msg['Subject'] = 'Information regarding PyCon Sweden 2025'
        msg['From'] = f'{my_email}'
        msg['To'] = f'{address}'
        msg['Cc'] = 'board@pycon.se'
        contact_name = contactdata["name"]
        contact_email = contactdata["email"]
        contact_mobile = contactdata["mobile"]
        print("Subject:", msg['Subject'])

        contact_others = ""
        for k, v in contactdata["others"].items():
            contact_others += f" * {k}: {v}\n" 

        msgPlain = f'''Hi {author},


* Your ticket for the conference: {promocode}.

You can use the link below to enter the shop:

        {promolink}

and register yourself. It is important for us in order
to control catering and generate your speaker badge.
You're entitled to only ONE ticket.


* Contact

Your point of contact for the conference will be {contact_name}.
You can reach me via in the following ways:
 * mobile: {contact_mobile}
 * email: {contact_email}
{contact_others}

We would like you to share your mobile phone so we can reach you
if necessary during the event.


* Program and time slot

In case you didn't check yet, we've released our program in
our website.  You can check there your talk date and time.

    https://pycon.se/#program


* About the presentations

If you represent a company or want to show your company
please use maximum 2 slides for it and no more than 5 minutes.
The conference focus is Python and it shouldn't be used
for advertisement.  So please keep this policy in mind during
your talk.

There is no template and we don't store the presentations.
You can decide whatever template that suits better for your
presentation slides.


* Regarding the presentation technicalities

You can use resolution 1080p for your presentation (1920x1080 px).
We expect to have HDMI and USB-C connector for the equipment, but
we will confirm it on Wednesday.

There will be wifi provided by the venue as well.

We don't store the presentations, so you don't need to send it to
us in advance.  All presentations will be recorded at main 
auditorium.  Videos will be released next year, but we don't
have yet a specific date about it.



* Tips about presenting at the stage

There is no good manual or handbook for that, but we can recommend the
good "how to avoid death by powerpoint" with very clear points how
to make great presentations.

      https://youtu.be/Iwpi1Lm6dFo?si=vAjAQUun5dpLOxhK



* About the venue

Conference will be held at Clarion Hotel Stockholm, at Skanstull
served by subway green line.  It is close to T-Centralen, main station
located in Stockholm.

More info about the location:  
https://clarion-stockholm-hotel.hotel-ds.com/en/

We will be at the venue on Wednesday, 29 October, from 4-6 pm
to meet organization personel and prepare for next day.  
You're welcome to meet us there too and give a try on the 
equipment for presentation.

If you can't make it on Wednesday, please try to check your
equipment or before the conference begins, at 8 am, or during 
the coffee breaks.  We can also check at the end of first day.


 * Credentials

There will be a badge with your name at the entrance.  If you
attend the gattering on Wednesday you can also fetch it there.


 * Speakers photo

We will try to have a photo with as much speakers as possible on
30 October at lunch time (around 12:00).  Please stay at the
auditorium when lunch time starts for it.  It will take only 5
minutes.


* Halloween party

This year we will have a mingle with Halloween themed party.
It will happen in a bar on Odenplan (reachable by subway)
on Friday after the conference.
So bring your best costume,  be scarry 🎃, and have fun.
Admitance is free of charge for speakers.


Best Regards,
PyCon Sweden 2025 organization board
'''
        msg['Cc'] = 'board@pycon.se'
        print(msgPlain)
        msg.attach(MIMEText(msgPlain, 'plain'))
        raw = base64.urlsafe_b64encode(msg.as_bytes())
        raw = raw.decode()
        body = {'raw': raw}

        if not dryrun:
            message1 = body
            message = (service.users().messages().send(
                userId="me", body=message1).execute())

            print(f'Message Id: {message["id"]} to {email} sent')
        else:
            print("Dry-run mode")
            print(f'Message Id: {email} would be sent')
        print('====')

def get_contact(speakers_json: dict, speaker_name: str) -> dict|None:
    """
     3   │     "ID": "123456",
     4   │     "Name": "Julius Cezar",
     5   │     "Email": "julius_cezar@hl.eng.br",
     6   │     "Proposal IDs": [
     7   │       "ABCDEF",
     8   │       "GHIJKL"
     9   │     ],
    10   │     "Proposal titles": [
    11   │       "Python for emperors",
    12   │       "Using Python to conquer the world"
    13   │     ]
    14   │   },
    """
    for data in speakers_json:
        if data["Name"] == speaker_name:
            return data
    # not found
    return None

if __name__ == '__main__':
    parse = argparse.ArgumentParser(
        description="Script to send information to all speakers")
    parse.add_argument(
        "--pretalxjson",
        required=True,
        help=
        "The JSON file dumped from Pretalx with speakers information"
    )
    parse.add_argument("--pretixcodes",
                       required=True,
                       help="Pretix promocode CSV to send for speakers")
    parse.add_argument(
        "--contactjson",
        required=True,
        help=
        "Details from contact in a JSON file (to avoid exposing information in the Internet"
    )
    parse.add_argument("--dryrun",
                       action='store_true',
                       default=False,
                       help="Run for real or just show the output")
    parse.add_argument("--pickleconf",
                       required=True,
                       help="The gmail configuration in a pickle file format")
    args = parse.parse_args()

    # Get the path to the pickle file

    # Load our pickled credentials
    creds = pickle.load(open(args.pickleconf, 'rb'))

    # Build the service
    service = googleapiclient.discovery.build('gmail', 'v1', credentials=creds)

    with open(args.contactjson) as fd:
        contact_data = json.load(fd)

    with open(args.pretalxjson) as fd:
        speakersJSON = json.load(fd)

    with open(args.pretixcodes, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            # Name,Role,Voucher,Link,Send,Redeem,,Name,Role,Voucher,Link
            if row['Name'] is None or len(row['Name']) == 0:
                continue
            data = get_contact(speakersJSON, row['Name'])
            if data is None:
                print(f"WARNING: {row['Name']} not found")
                continue
            sendMail(row, data, contact_data, args.dryrun,
                         service)

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


def sendMail(data, promocode, contactdata, dryrun, service):
    # Create a message
    my_email = 'info@pycon.se'
    author = data['Your name']
    email = data['Email Address']
    other_email = data['Additional speakers']
    for address in [email, other_email]:
        if address == "":
            continue
        print("Address:", address)
        msg = MIMEMultipart('alternative')
        msg['Subject'] = 'Information regarding PyCon Sweden 2023'
        msg['From'] = f'{my_email}'
        msg['To'] = f'{address}'
        msg['Cc'] = 'board@pycon.se'
        msgPlain = f'''Hi {author},
* Your ticket for the conference

Please get into eventbrint link, and use the promo-code:

        {promocode}

and register yourself.  It is important for us in order
to control catering and generate your speaker badge.
You're entitled to only ONE ticket.

https://www.eventbrite.com/e/pycon-sweden-2023-tickets-661650052117

* Contact

{contactdata}

We would like you to share your mobile phone so we can reach you
if necessary during the event.

* Program and time slot

In case you didn't check yet, we've released our program in
our website.  You can check there your talk date and time.

    https://www.pycon.se/#program

* About the presentations

If you represent a company or want to show your company
please use maximum 2 slides for it and no more than 5 minutes.
The conference focus is Python and it shouldn't be used
to advertisement.  So please keep this policy in mind during
your talk.

There is no template and we don't store the presentations.
You can decide whatever template that suits better for your
presentation slides.

* Regarding the presentation technicalities

You can use resolution 1080p for your presentation (1920x1080 px).
We expect to have HDMI and USB-C connector for the equipment, but
we will confirm it on Wednesday.

There will be wifi provided by Hilton as well.

We don't store the presentations, so you don't need to send it to
us in advance.  All presentations will be recorded at main 
auditorium.  Videos will be released next year, but we don't
have yet a specific date about it.


* Tips about presenting at the stage

There is good manual or handbook for that, but we can recommend the
good "how to avoida death by powerpoint" with very clear points how
to make great presentations.

      https://youtu.be/Iwpi1Lm6dFo?si=vAjAQUun5dpLOxhK

* About the venue

Conference will be held at Hilton Slussen hotel, at Slussen
station served by subway green and red lines.  It is close to
T-Centralen, main station located in Stockholm.

More info about the location:  
https://www.hilton.com/en/hotels/stoslhi-hilton-stockholm-slussen/

We will be at Hilton on Wednesday, November 8th, around 4 pm
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
November 8th at lunch time (around 12:00).  Please stay at the
auditorium when lunch time starts for it.  It will take only 5
minutes.

Best Regards,
PyCon Sweden 2023 organization board
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


if __name__ == '__main__':
    parse = argparse.ArgumentParser(
        description="Script to send information to all speakers")
    parse.add_argument(
        "--csvfile",
        required=True,
        help=
        "The CSV file dumped from Google spreadsheet with speakers information"
    )
    parse.add_argument("--promocode",
                       required=True,
                       help="EventBrite promocode to send for speakers")
    parse.add_argument(
        "--contactfile",
        required=True,
        help=
        "Details from contact in a file (to avoid exposing information in the Internet"
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

    with open(args.contactfile) as fd:
        contact_data = fd.read().rstrip()

    with open(args.csvfile, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            if row['Confirmed'].lower() == "yes":
                sendMail(row, args.promocode, contact_data, args.dryrun,
                         service)

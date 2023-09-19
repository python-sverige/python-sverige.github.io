#! /usr/bin/env python3
# src: https://scriptreference.com/sending-emails-via-gmail-with-python/
import pickle
import os
import base64
import googleapiclient.discovery
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv
import argparse

PYCONSE_DAYS = "November 9-10"
PYCONSE_YEAR = "2023"
PYCONSE_LOCATION = "Hilton Slussen hotel in Stockholm"

# Get the path to the pickle file
home_dir = os.path.expanduser('~')
pickle_path = os.path.join(home_dir, 'gmail.pickle')

# Load our pickled credentials
creds = pickle.load(open(pickle_path, 'rb'))

# Build the service
service = googleapiclient.discovery.build('gmail', 'v1', credentials=creds)


def sendMail(data, dryrun=True):
    # Create a message
    my_email = 'info@pycon.se'
    author = data['Your name']
    title = data['Talk/Workshop title']
    cfp_type = data['Proposal type']
    email = data['Email Address']
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f'Your {cfp_type} "{title}" wasn\'t accepted for PyCon Sweden {PYCONSE_YEAR}'
    msg['From'] = f'{my_email}'
    msg['To'] = f'{email}'
    msg['Cc'] = 'board@pycon.se'
    msgPlain = f'''Hi {author},

Unfortunately we reached the decision to not accept your {cfp_type}
titled "{title}" this time.

It wasn't an easy decision and we were very sorry to not get you as
speaker.  And we hope you don't get frustrated and continue contributing
to Python community.

As part of our consideration to all authors that submitted a proposal
we can offer a discounted business ticket for this year's conference
at the same price as early bird. If you are interested in such ticket,
please reply this mail to let us know.  These tickets are limited in
number and we can provide only some of them in the format "first
come, first served".

Thank you for your time applying for the Call of Proposals for this
year's conference.

Best Regards,
PyCon Sweden {PYCONSE_YEAR} organization board
'''
    #msgHtml = msgPlain
    print(msgPlain)
    msg.attach(MIMEText(msgPlain, 'plain'))
    #msg.attach(MIMEText(msgHtml, 'html'))
    raw = base64.urlsafe_b64encode(msg.as_bytes())
    raw = raw.decode()
    body = {'raw': raw}

    if not dryrun:
        print("NOT DRY-RUN")
        print(f"sending email to {email}")
        message1 = body
        message = (service.users().messages().send(userId="me",
                                                   body=message1).execute())

        print(f'Message Id: {message["id"]} to {email} sent')
    else:
        print("Dry-run mode - nothing sent")
        print(f"It would send email to {email}")
    print('====')


parse = argparse.ArgumentParser(
    description=
    "Script to send authors information that their talk was rejected")
parse.add_argument("--csvfile",
                   required=True,
                   help="Export CSV file with CFP information")
parse.add_argument("--dryrun",
                   action='store_true',
                   help="Set this flag to just print the result")
args = parse.parse_args()

with open(args.csvfile, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        if row["Status"] == "Rejected":
            sendMail(row, args.dryrun)

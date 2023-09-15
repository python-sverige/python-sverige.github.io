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
    abstract = data['Abstract']
    cfp_type = data['Proposal type']
    email = data['Email Address']
    bio = data['Your biography']
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f'Your {cfp_type}: {title} -  has been selected for PyCon Sweden {PYCONSE_YEAR}'
    msg['From'] = f'{my_email}'
    msg['To'] = f'{email}'
    msg['Cc'] = 'board@pycon.se'
    msgPlain = f'''Hi {author},

Your {cfp_type} "{title}" was selected to be presented in 
PyCon Sweden {PYCONSE_YEAR}.

The conference will be held at {PYCONSE_LOCATION}
on {PYCONSE_DAYS}.

Please reply this mail confirming you can make the presentation.

If you need to update your {cfp_type} information, please include the
updated version in your reply.  Otherwise they will published in an
automated way in the same way as in you sent.

Your {cfp_type} details:

Title: {title}

Abstract:
{abstract}

Bio:
{bio}

Best Regards,
PyCon Sweden {PYCONSE_YEAR} organization board
'''
    #msgHtml = msgPlain
    print(msgPlain)
    msg.attach(MIMEText(msgPlain, 'plain'))
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
        print("Dry-Run mode - nothing sent")
        print(f"It would send email to {email}")
    print('====')


parse = argparse.ArgumentParser(
    description=
    "Script to send authors information that their talk was selected")
parse.add_argument("--csvfile",
                   required=True,
                   help="Export CSV file with CFP information")
parse.add_argument(
    "--dryrun",
    type=bool,
    default=True,
    help="Select false to send the emails or it will just print the result")
args = parse.parse_args()

with open(args.csvfile, newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        if row["Status"] == "Accepted":
            sendMail(row, args.dryrun)

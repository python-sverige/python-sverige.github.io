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


# Get the path to the pickle file
home_dir = os.path.expanduser('~')
pickle_path = os.path.join(home_dir, 'gmail.pickle')

# Load our pickled credentials
creds = pickle.load(open(pickle_path, 'rb'))

# Build the service
service = googleapiclient.discovery.build('gmail', 'v1', credentials=creds)

def sendMail(data, dry_run=False):
    # Create a message
    my_email = 'info@pycon.se'
    author = data['author']
    title = data['title']
    abstract = data['abstract']
    cfp_type = data['cfp_type']
    youtube = data['YouTube']
    email = data['email']
    if youtube is None or len(youtube) == 0:
        print(f'No YouTube link to send to: {author}') 
        return
    # detect multiple emails:
    multiple_emails = email.split()
    if len(multiple_emails) > 1:
        for email in multiple_emails:
            data['email'] = email
            sendMail(data)
        # stop here
        return
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f'Your video from PyCon Sweden 2022 is on YouTube: {title}'
    msg['From'] = f'{my_email}'
    msg['To'] = f'{email}'
    msg['Cc'] = 'board@pycon.se'
    msgPlain = f'''Hi {author},

First of all we thank you for your participation in PyCon Sweden 2022
conference.  We couldn't make it happen without you.

We apologize for the long time to release the videos, but now they're online.
They're online but "unlisted".  So only people with link has access to it.

Your talk: {title}
Your video is here:  {youtube}

Please review the video and give us a feedback if it is ok to be released or
in case it needs some adjustments.

Best Regards,
PyCon Sweden 2022 organization board
'''
    #msgHtml = msgPlain
    print(msgPlain)
    msg.attach(MIMEText(msgPlain, 'plain'))
    #msg.attach(MIMEText(msgHtml, 'html'))
    raw = base64.urlsafe_b64encode(msg.as_bytes())
    raw = raw.decode()
    body = {'raw': raw}

    message1 = body

    if dry_run is False:
        message = (
            service.users().messages().send(
                userId="me", body=message1).execute())
        print(f'Message Id: {message["id"]} to {email} sent')

    print(f'Message Id: {email} sent')
    print('====')


with open(sys.argv[1], newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        if row['author'] in [ "Jim Dowling", "Ivica Kolenkaš", "Krishna Kalyan", "Valerio Maggio", "Dash Desai" ]:
            continue
        sendMail(row, dry_run=False)


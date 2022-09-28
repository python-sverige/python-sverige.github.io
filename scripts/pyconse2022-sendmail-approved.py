#! /usr/bin/env python3
# src: https://scriptreference.com/sending-emails-via-gmail-with-python/
import pickle
import os
import base64
import googleapiclient.discovery
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv


# Get the path to the pickle file
home_dir = os.path.expanduser('~')
pickle_path = os.path.join(home_dir, 'gmail.pickle')

# Load our pickled credentials
creds = pickle.load(open(pickle_path, 'rb'))

# Build the service
service = googleapiclient.discovery.build('gmail', 'v1', credentials=creds)

def sendMail(data):
    # Create a message
    my_email = 'info@pycon.se'
    author = data['author']
    title = data['title']
    abstract = data['abstract']
    cfp_type = data['cfp_type']
    email = data['email']
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f'Your {cfp_type} has been selected for PyCon Sweden 2022'
    msg['From'] = f'{my_email}'
    msg['To'] = f'{email}'
    msg['Cc'] = 'board@pycon.se'
    msgPlain = f'''Hi {author},

Your {cfp_type} "{title}" was selected to be presented in 
PyCon Sweden 2022.

The conference will be held at Hilton Slussen hotel in Stockholm
on November 2th-3rd.

Please reply this mail confirming you can make the presentation.

If you need to update your {cfp_type} title or abstract, please include the
updated version in your reply.

Your {cfp_type} details:

Title: {title}

Abstract:
{abstract}

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
    message = (
        service.users().messages().send(
            userId="me", body=message1).execute())

    print(f'Message Id: {message["id"]} to {email} sent')
    #print(f'Message Id: {email} sent')
    print('====')


with open("pyconse2022-selected-authors.csv", newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        sendMail(row)


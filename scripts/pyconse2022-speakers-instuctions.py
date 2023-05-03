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

def sendMail(data):
    # Create a message
    my_email = 'info@pycon.se'
    author = data['author']
    title = data['title']
    abstract = data['abstract']
    cfp_type = data['cfp_type']
    email = data['email']
    # detect multiple emails:
    multiple_emails = email.split()
    if len(multiple_emails) > 1:
        for email in multiple_emails:
            data['email'] = email
            sendMail(data)
        # stop here
        return
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f'Information regarding PyCon Sweden 2022'
    msg['From'] = f'{my_email}'
    msg['To'] = f'{email}'
    msg['Cc'] = 'board@pycon.se'
    msgPlain = f'''Hi {author},

* Program and time slot

In case you didn't check yet, we've released our program in
our website.  You can check there your talk date and time.

    https://www.pycon.se/#program

* About the venue

Conference will be held at Hilton Slussen hotel, at Slussen
station served by subway green and red lines.  It is close to
T-Centralen, main station located in Stockholm.

More info about the location:  
https://www.hilton.com/en/hotels/stoslhi-hilton-stockholm-slussen/

We will be at Hilton on Wednesday, November 2nd, around 4 pm
to meet organization personel and prepare for next day.  
You're welcome to meet us there too and give a try on the 
equipment for presentation.

If you can't make it on Wednesday, please try to check your
equipment or before the conference begins, at 9 am, or during 
the coffee breaks.  We can also check at the end of first day.

* Regarding the presentation

You can use resolution 1080p for your presentation (1920x1080 px).
We expect to have HDMI and USB-C connector for the equipment, but
we will confirm it on Wednesday.

There will be wifi provided by Hilton as well.

We don't store the presentations, so you don't need to send it to
us in advance.  All presentations will be recorded at main 
auditorium.  Videos will be released next year, but we don't
have yet a specific date about it.

 * Credentials

There will be a badge with your name at the entrance.  If you
attend the gattering on Wednesday you can also fetch it there.


 * Speakers photo

We will try to have a photo with as much speakers as possible on
November 3rd at lunch time.  Please stay at the auditorium when
lunch time starts for it.  It will take only 5 minutes.

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


with open(sys.argv[1], newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        if row['author'] in [ "Jim Dowling", "Ivica Kolenkaš", "Krishna Kalyan", "Valerio Maggio", "Dash Desai" ]:
            continue
        sendMail(row)


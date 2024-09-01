#! /usr/bin/env python3

import argparse
import csv
import os
import pickle
import base64
import googleapiclient.discovery
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Get the path to the pickle file
home_dir = os.path.expanduser('~')
pickle_path = os.path.join(home_dir, '.ssh', 'gmail.pickle')

# Load our pickled credentials
creds = pickle.load(open(pickle_path, 'rb'))

# Build the service
service = googleapiclient.discovery.build('gmail', 'v1', credentials=creds)


class Communicator:
    """
    Send email communication to attendees from past editions.
    CSV parsed here is generated by EventBrite.
    """
    def __init__(self):
        parser = argparse.ArgumentParser(
            "Send communication message to attendees from "
            "past PyCon editions using the CSV generated by EventBrite")
        parser.add_argument("--csvfile", 
                            required=True,
                            help="The CSV file generated by EventBrite with attendees information")
        parser.add_argument("--message", 
                            required=True,
                            help="The message to be sent into the e-mail body")
        self.args = parser.parse_args()

    def _readData(self):
        emails = []
        with open(self.args.csvfile) as csvfile:
            eventbrite = csv.DictReader(csvfile)
            for row in eventbrite:
                email = row['Attendee email']
                if not email in emails:
                    emails.append(email)
                    print(email)
                else:
                    print("Repeated:", email)
        self.attendees = sorted(emails)

    def sendMessage(self):
        import sys
        my_email = 'info@pycon.se'
        subject = 'Information about PyCon Sweden 2024'
        with open(self.args.message) as msg:
            msgPlain = msg.read()
        #print(msgPlain)
        self._readData()
        for email in self.attendees:
            if email is None or email == "":
                continue
            print("Sending message to:", email)
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['To'] = email
            msg['From'] = my_email
            msg.attach(MIMEText(msgPlain, 'plain'))
            raw = base64.urlsafe_b64encode(msg.as_bytes())
            raw = raw.decode()
            body = {'raw': raw}
            print(body)
            message1 = body
            message = (service.users().messages().send(userId="me",
                                                   body=message1).execute())


if __name__ == '__main__':
    com = Communicator()
    com.sendMessage()



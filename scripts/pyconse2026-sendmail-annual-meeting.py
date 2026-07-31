#! /usr/bin/env -S uv run --script
#
# /// script
# dependencies = [
# "google-api-python-client",
# "google-auth-httplib2",
# "google-auth-oauthlib",
# "coloredlogs"
# ]
# ///

# src: https://scriptreference.com/sending-emails-via-gmail-with-python/
import pickle
import os
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv
import argparse
import time
import logging

import googleapiclient.discovery
import coloredlogs

# Note: export the result of the PyCon Sverige form
# from here: https://docs.google.com/forms/d/1UTFIi0saX3o4ebsQDOzqkAC_h4IKSzuaZV81llfVcJA/edit#responses

DAYS = {
    "en": "3 of September",
    "sv": "3:e september"
}
YEAR = time.strftime("%Y", time.localtime())
TIME = "20:00"


logging.root.setLevel(logging.INFO)
scriptName = os.path.basename(__file__)
logger = logging.getLogger(scriptName)
logger.setLevel('INFO')
coloredlogs.install(logger=logger)


def sendMail(data: dict[str,str], service, dryrun: bool = True):
    # Create a message
    my_email = 'Helio@Loureiro.eng.br'
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f'Kallelse till årsmöte för Python Sverige {YEAR} - Notice of annual meeting for Python Sweden {YEAR}'
    msg['From'] = f'{my_email}'
    email = data['Email']
    msg['To'] = email
    msgPlain = f'''

Message follows in English

Kallelse till årsmöte för Python Sverige {YEAR}.

Ett extra årsmöte för att fastställa förra årets ekonomiska rapport kommer.
att hållas i online den {DAYS["sv"]} klockan {TIME}. Agenda återfinns sist i detta mail.

Föreningens stadgar och tidigare protokoll kan hittas på
github.com/python-sverige

En länk till online mötet kommer att skickas ut senare.

Välkommna!

Agenda för årsmötet:

1    Val av mötesordförande
2    Val av mötessekreterare
3    Val av två personer att jämte mötesordföranden justera årsmötets protokoll
4    Fastställande av föredragningslistan
5    Fastställande av röstlängd
6    Godkännande av kallelse
7    Styrelsens ekonomiska berättelse över det senaste året
8    Revisorernas berättelse
9    Fråga om fastställande av balansräkning samt disposition av årets resultat
10   Fråga om ansvarsfrihet för styrelsens ledamöter
11   Mötets avslutande

Helio Loureiro
Board member, Python Sverige

------

Notice of annual meeting for Python Sweden {YEAR}.

An yearly meeting to finalize the financial reports.
will be held online on the {DAYS["en"]}, 0. Agenda can be found at the end of this email.

Bylaws and earlier protocols can be found at github.com/python-sverige

A link to the online meeting will be sent out later.

Welcome!

Agenda for the annual meeting:

1 Election of chairman of the meeting
2 Election of meeting secretary
3 Election of two people to adjust the annual meeting together with the chairman of the meeting protocol
4 Setting the agenda
5 Determination of voting list
6 Approval of summons
7 The Board's financial report over the past year
8 The accountants' information
9 Question about fixing the balance sheet and disposition of the year results
10 Question on discharge from the board of directors
11 End of meeting

Helio Loureiro
Board member, Python Sverige
'''
    #msgHtml = msgPlain
    logger.debug(msgPlain)
    msg.attach(MIMEText(msgPlain, 'plain'))
    raw = base64.urlsafe_b64encode(msg.as_bytes())
    raw = raw.decode()
    body = {'raw': raw}

    if not dryrun:
        logger.warning("NOT DRY-RUN")
        logger.info(f"sending email to {email}")
        message1 = body
        message = (service.users().messages().send(userId="me",
                                                   body=message1).execute())

        logger.info(f'Message Id: {message["id"]} to {email} sent')
    else:
        logger.warning("Dry-Run mode - nothing sent")
        logger.info(f"It would send email to {email}")
    logger.info('==== done ====')


parse = argparse.ArgumentParser(
    description=
    "Script to send authors information that their talk was selected")
parse.add_argument("--csvfile",
                   required=True,
                   help="Export CSV file with CFP information")
parse.add_argument("--dryrun",
                   action='store_true',
                   help="Set this flag to just print the result")
parse.add_argument("--pickle", help="Pickle authorization file")
parse.add_argument("--loglevel", default="info", help="Logging level (default=info)")

args = parse.parse_args()

if args.loglevel != "info":
    logger.info(f"Changing logging level to: {args.loglevel}")
    logger.setLevel(args.loglevel.upper())
    coloredlogs.install(logger=logger)

if args.pickle is None:
    # Get the path to the pickle file
    home_dir = os.path.expanduser('~')
    pickle_path = os.path.join(home_dir, 'gmail.pickle')
else:
    pickle_path = args.pickle

# Load our pickled credentials
with open(pickle_path, 'rb') as fh:
    creds = pickle.load(fh)

# Build the service
service = googleapiclient.discovery.build('gmail', 'v1', credentials=creds)


error_csv = args.csvfile.replace(".csv", "-error.csv")
with open(args.csvfile, newline='', encoding='utf-8') as csvfile, open(error_csv, 'w', newline='', encoding='utf-8') as csvwrite:
    csvreader = csv.DictReader(csvfile)
    csvwriter = csv.writer(csvwrite, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in csvreader:
        try:
            sendMail(row, service, args.dryrun)
            time.sleep(60)
        except googleapiclient.errors.HttpError:
            logger.error(f"Failed to send email to: {row['Email']}")
            csvwriter.writerow(row)

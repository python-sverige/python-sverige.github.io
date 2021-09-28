#! /usr/bin/python3 -u

import argparse
import configparser
import sys, os
import csv

def message(from, to, subject, name, title, talk_grp, description, area, level,bio):
    """
    Create mail message to be sent.
    It stays on top and has several arguments, but makes life easier for
    the ones writting the mail message. Hopefully.
    """

    msg = f"From: {from}\n"
    msg += f"To: {to}\n"
    msg += f"Subject: {subject}\n"
    msg += f"""
Dear {name},

You {talk_grp} has been selected to be presented at PyCon Sweden 2020.

It will be displayed as follow:

Title: {tile}

Type: {talk_grp}

Description: {description}

Level: {level}

author: {name}

Bio: {bio}


We will be publishing the schedule soon.

You will have the option to submit your talk in advance as recorded video.
In order to do this, use minimal resolution 720p and format 16:9 or 16:10.

In case you want to present it online, we will use platform StreamYard
to held the conference.  It is web based site.  We will have a group test
for rehearsal for you to get familiar with its usage.

In case you need to change any information on your presentation, please
contact us.


Thanks for your participation,
PyCon Sweden 2020 board

-= This is an automated message =-
"""

    return msg


def debug(*msg):
    if os.environ.get("DEBUG"):
        print(*msg)

class EmailNotifySpeakers:
    def __init__(self, csv_file, config_file):
        "Prepare structures to use"
        self.csv_file = csv_file
        self.config_file = config_file
        self.talks = {}
        self.read_configuration()

    def read_data(self):
        "Read the configuration from CSV file"
        talks = {}
        with open(self.csv_file) as csv_stream:
            csv_data = csv.reader(csv_stream)
            counter = 0
            for row in csv_data:
                talks[counter] = {
                    "speaker" : row[7],
                    "title" : row[4],
                    "bio" : row[9],
                    "email" : row[8],
                    "type" : row[0],
                    "area" : row[1],
                    "description" : row[5],
                }
                debug(talks[counter])
                counter += 1
        self.talks = talks

    def read_configuration(self):
        "Read mail server and account settings"
        debug("read_configuration():")
        conf = configparser.ConfigParser()
        conf.read(self.config_file)
        self.mailservice = {
            "smtp_server" : conf.get("Default", "smtpserver"),
            "smtp_port" : conf.get("Default", "smtpport"),
            "fullname" : conf.get("Default", "name"),
            "email" : conf.get("Default", "email"),
            "username" : conf.get("Default", "username"),
            "password" : conf.get("Default", "password")
        }
        debug(" smtp_server:", self.mailservice["smtp_server"])
        debug(" smtp_port:", self.mailservice["smtp_port"])
        debug(" fullname:", self.mailservice["fullname"])
        debug(" email:", self.mailservice["email"])
        debug(" username:", self.mailservice["username"])
        debug(" password:", self.mailservice["password"])

    def send(self):


if __name__ == '__main__':
    "Parsing command line here"

    parser = argparse.ArgumentParser(description="It sends mail notification to talks/workshops authors")
    parser.add_argument("--csv", help="CSV file with forms answers")
    parser.add_argument("--conf", help="Configuration File")
    args = parser.parse_args()

    if args.csv == None or args.conf == None:
        parser.print_help()
        sys.exit(os.EX_NOINPUT)

    mails = EmailNotifySpeakers(args.csv, args.conf)
    mails.read_data()
    mail.send()

#! /usr/bin/env python3
import pickle
import os
from google_auth_oauthlib.flow import InstalledAppFlow


# Specify permissions to send and read/write messages
# Find more information at:
# https://developers.google.com/gmail/api/auth/scopes
SCOPES = ['https://www.googleapis.com/auth/gmail.send',
          'https://www.googleapis.com/auth/gmail.modify']


# Get the user's home directory
home_dir = os.path.expanduser('~')

# Recall that the credentials.json data is saved in our "Downloads" folder
json_path = os.path.join(home_dir, '.ssh', 'pyconse-email-oauth2.json')

# Next we indicate to the API how we will be generating our credentials
flow = InstalledAppFlow.from_client_secrets_file(json_path, SCOPES)

# This step will generate the pickle file
# The file gmail.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
creds = flow.run_local_server(port=0)

# We are going to store the credentials in the user's home directory
pickle_path = os.path.join(home_dir, 'gmail.pickle')
with open(pickle_path, 'wb') as token:
    pickle.dump(creds, token)

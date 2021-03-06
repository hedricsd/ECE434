#!/usr/bin/env python3
# Based pm: https://github.com/googleworkspace/python-samples/tree/master/sheets/quickstart
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START sheets_quickstart]
from __future__ import print_function
import pickle
import os.path
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import time, sys

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1FF3IfO-Dlb1PZvrRaW4pJE21VSg9_GEUsmOtegPw4h4'
SAMPLE_RANGE_NAME = 'A2'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    
    temp1 = os.open("/sys/class/hwmon/hwmon0/temp1_input", os.O_RDONLY);
    temp1Value = os.read(temp1, 6);
    temp1Value = temp1Value.decode("utf-8")
    
    temp2 = os.open("/sys/class/hwmon/hwmon1/temp1_input", os.O_RDONLY);
    temp2Value = os.read(temp2, 6);
    temp2Value = temp2Value.decode("utf-8")
    
    temp3 = os.open("/sys/class/hwmon/hwmon2/temp1_input", os.O_RDONLY);
    temp3Value = os.read(temp3, 6);
    temp3Value = temp3Value.decode("utf-8")
    
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            # creds = flow.run_local_server(port=0)
            creds = flow.run_console()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    values = [ [time.time()/60/60/24+ 25569 - 4/24, int(temp1Value)/1000, int(temp2Value)/1000, int(temp3Value)/1000]]
    body = {'values': values}
    result = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME,
                                valueInputOption='USER_ENTERED', 
                                body=body
                                ).execute()
    print(result)

if __name__ == '__main__':
    main()
# [END sheets_quickstart]

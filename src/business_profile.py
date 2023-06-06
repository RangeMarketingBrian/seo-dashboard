import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json

def get_creds(CLIENT_FILE, SCOPES):
    """Get API credentials using client file and API scopes."""
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
            
    return creds

def businessprofile_request(creds):
    with build("businessprofileperformance", "v1", credentials=creds) as service:
        request = service.locations().fetchMultiDailyMetricsTimeSeries(location='locations/15699770951958109547', dailyMetrics='BUSINESS_IMPRESSIONS_DESKTOP_SEARCH', dailyRange_endDate_day=0, dailyRange_endDate_month=0, dailyRange_endDate_year=0, dailyRange_startDate_day=0, dailyRange_startDate_month=0, dailyRange_startDate_year=2023)
        
        try:
            response = request.execute()
            
            print(json.dumps(response, sort_keys=True, indent=4))
        except HttpError as e:
            print('Error response status code : {0}, reason : {1}'.format(e.status_code, e.error_details))
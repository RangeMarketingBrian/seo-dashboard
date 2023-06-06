from src.business_profile import *

CLIENT_FILE = 'brian_seo_client.json'
SCOPES = ['https://www.googleapis.com/auth/business.manage']

creds = get_creds(CLIENT_FILE, SCOPES)
businessprofile_request(creds)
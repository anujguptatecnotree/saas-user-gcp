import requests
import json
import os


import google.auth
import google.auth.transport.requests
from google.oauth2 import service_account


#os.system("gcloud auth activate-service-account --key-file=/home/anujgupta/gcp_login/ser.json")
credentials = service_account.Credentials.from_service_account_file('/home/anujgupta/gcp_login/ser.json',  scopes=['https://www.googleapis.com/auth/cloud-platform'])
auth_req = google.auth.transport.requests.Request()
credentials.refresh(auth_req)
token = credentials.token
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + f"{token}"
}

account_id = "a74c9fc9-ebe9-4f77-bfd5-1c767ef4842a"


response = requests.get(f'https://cloudcommerceprocurement.googleapis.com/v1/providers/juniper-marketplace/accounts/', headers=headers)
account_details = response.json()['accounts'][0]
account_id = account_details['name'].split('/')[-1]
state = account_details['state']
approvals = account_details['approvals']
print(approvals)
print(account_id)
print(state)

from django.shortcuts import render, redirect
from accounts.models import userAccounts
import json, os
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
#Google Auth 
import requests
import google.auth
import google.auth.transport.requests
from google.oauth2 import service_account

#JWT 
import jwt

dict = {}
# Create your views here.



def generate_token():
    credentials = service_account.Credentials.from_service_account_file('/home/anujgupta/gcp_login/ser.json', scopes=['https://www.googleapis.com/auth/cloud-platform'])
    auth_req = google.auth.transport.requests.Request()
    credentials.refresh(auth_req)
    token  = credentials.token
    headers = {
       'Content-Type': 'application/json',
       'Authorization': 'Bearer ' + f"{token}"
    }
    user_auth = {'token': credentials.token, 'headers': headers}
    return user_auth

def juniper_index(request):
    if request.method == 'POST':
        token = request.POST.get('x-gcp-marketplace-token')
        payload = jwt.decode(token,options={"verify_signature": False})
        #print(payload)
        payload_in_json = json.dumps(payload)
        print(payload_in_json)
        #return render(request,'registeration.html')
        global dict
        dict = payload
        return HttpResponseRedirect('/register/')



def register(request):
    if request.method == 'POST':
        user_name = request.POST["username"]
        email_id = request.POST["email"]
        contact_num = request.POST["contact"]
        company_name = request.POST["company-name"]
        
        account_id = dict['sub']
        token = generate_token()

        user = userAccounts(username=user_name, email = email_id, contact = contact_num, company = company_name, account_id = account_id)
        user.save()

        return render(request,'successful.html')
    else:
        return render(request,'registeration.html')
    
        
def accounts_list(request):
    if request.method == 'GET':
        user_auth = generate_token() 
        token = user_auth['token']
        headers = user_auth['headers']
        response = requests.get(f'https://cloudcommerceprocurement.googleapis.com/v1/providers/juniper-marketplace/accounts/', headers=headers)
        account_details = response.json()['accounts']
        json_format = json.dumps(account_details, indent=4)  
    
        return HttpResponse(json_format, content_type="application/json")

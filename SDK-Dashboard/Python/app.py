from flask import *
import json
import requests
import asyncio
import os

app = Flask(__name__)

HOST = "http://192.168.10.47:8088"
DASHBOARD = "6e96c9aa-95f9-47f8-8046-fa764f94faaf"
USERNAME = "test"
PASSWORD = "test"

def guest_token(key: int):
    url = "http://192.168.10.47:8088/api/v1/security/guest_token/"
    payload = json.dumps({
        "resources": [
            {
            "id": str(DASHBOARD),
            "type": "dashboard"
            }
        ],
        "rls": [],
        "user": {
            "first_name": str(USERNAME),
            "last_name": str(USERNAME),
            "username": str(USERNAME)
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + str(key)
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()['token']

def login_token():
    url = "http://192.168.10.47:8088/api/v1/security/login"
    payload = json.dumps({
        "password": str(PASSWORD),
        "provider": "db",
        "refresh": True,
        "username": str(USERNAME)
    })
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    data = guest_token(response.json()['access_token'])
    return data

@app.route('/')
def index():
    call_api = login_token()
    pack_val = {"token": call_api, "host": HOST, "dashboard": DASHBOARD}
    return render_template("index.html", data=pack_val)
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
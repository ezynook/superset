from flask import *
import json
import requests
import asyncio
import os, sys
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

HOST = "http://192.168.10.47:8088"
DASHBOARD = "7af45060-8d1e-487f-9781-7855f06e6871"
USERNAME = "nook"
PASSWORD = "nook"

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
#Route เพื่อให้ Owner มา Call เพื่อรับ Guest Token
@app.route('/get_token', methods=["GET"])
def getresult():
    if not request.args.get('dashboard_id'):
        return jsonify({"message":"dashboard id is empty"})
        sys.exit(1)
        
    dashboard_id = request.args.get('dashboard_id')
    url = "http://192.168.10.47:8088/api/v1/security/login"
    payload = json.dumps({
        "password": "tang",
        "provider": "db",
        "refresh": True,
        "username": "tang"
    })
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    
    url = "http://192.168.10.47:8088/api/v1/security/guest_token/"
    payload = json.dumps({
        "resources": [
            {
            "id": dashboard_id,
            "type": "dashboard"
            }
        ],
        "rls": [],
        "user": {
            "first_name": "tang",
            "last_name": "tang",
            "username": "tang"
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + response.json()['access_token']
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()['token']

@app.route('/')
def index():
    call_api = login_token()
    pack_val = {"token": call_api, "host": HOST, "dashboard": DASHBOARD}
    return render_template("index.html", data=pack_val)

# @app.route('/script')
# def index():
#     call_api = login_token()
#     pack_val = {"token": call_api, "host": HOST, "dashboard": DASHBOARD}
#     return render_template("index.html", data=pack_val)
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)

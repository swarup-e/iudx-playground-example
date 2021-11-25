#!/usr/bin/env python3

import os
import requests
import json
import time

url = "https://keycloak.iudx.org.in/auth/realms/iudx/protocol/openid-connect/token"

payload=f'client_id=playground-client&grant_type=refresh_token&refresh_token={os.environ["KC_REFRESH_TOKEN"]}'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

with open('credentials.json', 'w', encoding='utf-8') as f:
    json.dump(response.json(), f, ensure_ascii=False, indent=4)

def run():
    while True:
        with open('credentials.json') as f:
            json_data = json.load(f)
            payload = f'client_id=playground-client&grant_type=refresh_token&refresh_token={json_data["refresh_token"]}'
        response = requests.request("POST", url, headers=headers, data=payload)
        with open('credentials.json', 'w', encoding='utf-8') as f:
            json.dump(response.json(), f, ensure_ascii=False, indent=4)
        time.sleep(120)

if __name__ == "__main__":
    run()

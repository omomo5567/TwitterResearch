import requests
import json
import api_key

api = api_key.api_key

url = "https://safebrowsing.googleapis.com/v4/threatMatches:find"
payload = {
    "client": {
        "clientId":      "yourcompanyname",
        "clientVersion": "1.5.2"
    },
    "threatInfo": {
        "threatTypes":      ["MALWARE", "SOCIAL_ENGINEERING"],
        "platformTypes":    ["WINDOWS"],
        "threatEntryTypes": ["URL"],
        "threatEntries": [
            {"url": "http://wrthwtj.duckdns.org"}
        ]
    }
}
params = {'key': api}
r = requests.post(url, params=params, json=payload)
# Print response
print(r)
print(r.json())

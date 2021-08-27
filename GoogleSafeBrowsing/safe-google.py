import requests
import json

api_key = 'AIzaSyCGMYii3NryUpvfv2RvOmw-elef-fpTqU4'
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
params = {'key': api_key}
r = requests.post(url, params=params, json=payload)
# Print response
print(r)
print(r.json())

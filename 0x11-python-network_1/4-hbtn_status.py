#!/usr/bin/python3

import requests

url = "https://alx-intranet.hbtn.io/status"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
    body = response.text
    print("- Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
except requests.HTTPError as e:
    print(f"Error fetching URL: {e}")


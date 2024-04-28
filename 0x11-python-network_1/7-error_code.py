#!/usr/bin/python3

import requests
import sys

# Extract URL from command-line argument
url = sys.argv[1]

try:
    response = requests.get(url)
    # Check if the status code is greater than or equal to 400
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        # Display the body of the response
        print(response.text)
except requests.RequestException as e:
    print("Error fetching URL:", e)


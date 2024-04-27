#!/usr/bin/python3

import urllib.request
import sys

# Extract URL from command-line argument
url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        # Check if the header "X-Request-Id" is present
        if 'X-Request-Id' in response.headers:
            request_id = response.headers['X-Request-Id']
            print("Value of X-Request-Id:", request_id)
        else:
            print("X-Request-Id header not found in the response.")
except urllib.error.URLError as e:
    print("Error fetching URL:", e)


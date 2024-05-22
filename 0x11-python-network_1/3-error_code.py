#!/usr/bin/python3

import urllib.request
import urllib.error
import sys

# Extract URL from command-line argument
url = sys.argv[1]

try:
    # Send request to the URL
    with urllib.request.urlopen(url) as response:
        # Read and decode the body of the response
        body = response.read().decode('utf-8')
        print(body)
except urllib.error.HTTPError as e:
    # Print the error code
    print("Error code:", e.code)



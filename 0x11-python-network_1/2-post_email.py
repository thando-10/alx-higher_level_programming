#!/usr/bin/python3

import urllib.request
import urllib.parse
import sys

# Extract URL and email from command-line arguments
url = sys.argv[1]
email = sys.argv[2]

# Encode the email parameter
data = urllib.parse.urlencode({'email': email}).encode('utf-8')

try:
    # Send POST request with email parameter
    with urllib.request.urlopen(url, data=data) as response:
        # Read and decode the body of the response
        body = response.read().decode('utf-8')
        print(body)
except urllib.error.URLError as e:
    print("Error fetching URL:", e)

python post_request.py http://0.0.0.0:5000/post_email hr@holbertonschool.com hr@holbertonschool.com


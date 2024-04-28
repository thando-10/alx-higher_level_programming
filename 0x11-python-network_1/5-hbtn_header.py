#!/usr/bin/python3

import requests
import sys

# Extract URL from command-line argument
url = sys.argv[1]

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
    # Check if the header "X-Request-Id" is present
    if 'X-Request-Id' in response.headers:
        request_id = response.headers['X-Request-Id']
        print("Value of X-Request-Id:", request_id)
    else:
        print("X-Request-Id header not found in the response.")
except requests.HTTPError as e:
    print(f"Error fetching URL: {e}")


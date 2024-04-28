#!/usr/bin/python3

import requests
import sys

# Extract the letter from the command-line arguments or set it to an empty string if no argument is given
if len(sys.argv) > 1:
    q = sys.argv[1]
else:
    q = ""

# Create a dictionary with the letter parameter
data = {'q': q}

# Send POST request to the specified URL with the letter parameter
try:
    response = requests.post("http://0.0.0.0:5000/search_user", data=data)
    response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)

    # Check if the response body is properly JSON formatted and not empty
    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
except requests.HTTPError as e:
    print("Error sending POST request:", e)


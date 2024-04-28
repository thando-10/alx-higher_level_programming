#!/usr/bin/python3

import requests
import sys

# Extract URL and email from command-line arguments
url = sys.argv[1]
email = sys.argv[2]

# Create a dictionary with the email parameter
data = {'email': email}

try:
    # Send POST request with email parameter
    response = requests.post(url, data=data)
    response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
    
    # Display the body of the response
    print(response.text)
except requests.HTTPError as e:
    print(f"Error fetching URL: {e}")


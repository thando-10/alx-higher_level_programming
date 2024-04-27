#!/bin/bash

import requests
import sys

# Check if URL argument is provided
if len(sys.argv) < 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
    body_size = len(response.content)
    print("Size of the response body:", body_size, "bytes")
except requests.RequestException as e:
    print("Error fetching URL:", e)


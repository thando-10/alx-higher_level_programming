#!/usr/bin/python3

import requests
import sys

# Extract GitHub username and personal access token from command-line arguments
username = sys.argv[1]
password = sys.argv[2]

# GitHub API endpoint to fetch user information
url = "https://api.github.com/user"

# Set up Basic Authentication with username and personal access token
auth = (username, password)

try:
    # Send GET request to the GitHub API endpoint with Basic Authentication
    response = requests.get(url, auth=auth)
    response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
    
    # Display the user's id from the response JSON
    user_id = response.json()['id']
    print("Your GitHub user id is:", user_id)
except requests.HTTPError as e:
    print("Error fetching user information:", e)


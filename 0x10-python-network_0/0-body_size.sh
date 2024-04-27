#!/usr/bin/python3
#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request to the URL and store the response body in a temporary file
response=$(curl -s -o response_body.txt "$1")

# Check if curl was successful
if [ $? -eq 0 ]; then
    # Get the size of the response body in bytes
    body_size=$(stat -c %s response_body.txt)
    echo "Size of the response body: $body_size bytes"
else
    echo "Failed to retrieve response from $1"
fi

# Clean up the temporary file
rm -f response_body.txt


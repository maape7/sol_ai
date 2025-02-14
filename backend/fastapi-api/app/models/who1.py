import requests
import json

# Replace with your actual API key
api_key = "your_api_key"
domain_name = "google.com"

# Construct the API URL
url = f"https://api.whoisfreaks.com/v1.0/whois?apiKey={api_key}&whois=live&domainName={domain_name}"

# Make the request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    whois_data = response.json()
    
    print(json.dumps(whois_data, indent=4))  # Pretty print the JSON output
else:
    print(f"Error: {response.status_code}", response.text)
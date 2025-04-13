import requests

# Load access token and instance URL
with open('token.txt', 'r') as f:
    lines = f.readlines()
    access_token = lines[0].strip()
    instance_url = lines[1].strip()

# Salesforce Contact creation endpoint
url = f'{instance_url}/services/data/v58.0/sobjects/Contact/'

# Example contact data
data = {
    "FirstName": "Shiva",
    "LastName": "Kumar",
    "Email": "shiva.kumar@example.com",
    "Phone": "9876543210"
}

headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:
    print("✅ Contact created successfully!")
    print("Salesforce ID:", response.json()['id'])
else:
    print("❌ Failed to create contact")
    print(response.status_code)
    print(response.text)

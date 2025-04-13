import requests
with open('token.txt', 'r') as f:
    lines = f.readlines()
    access_token = lines[0].strip()
    instance_url = lines[1].strip()

#List all objects
url = f'{instance_url}/services/data/v58.0/sobjects/'
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Salesforce Objects:")
    print(response.json())
else:
    print("API Error:", response.status_code)
    print(response.text)

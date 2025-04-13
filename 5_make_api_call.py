import requests

with open('token.txt', 'r') as f:
    access_token = f.readline().strip()
    instance_url = f.readline().strip()

url = f'{instance_url}/services/data/v58.0/query'
query = "SELECT Id, FirstName, LastName, Email FROM Contact"
params = {'q': query}

headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()
    for contact in data['records']:
        print(f"{contact['FirstName']} {contact['LastName']} - {contact['Email']}")
else:
    print("Error:", response.status_code)
    print(response.text)

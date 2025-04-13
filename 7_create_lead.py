import requests

access_token = '<your_access_token>'
instance_url = '<your_instance_url>'  # e.g., https://yourInstance.salesforce.com

# Step 2: Define the endpoint
create_contact_url = f'{instance_url}/services/data/v58.0/sobjects/Contact/'

# Step 3: Define the contact data to be created
contact_data = {
    "FirstName": "John",
    "LastName": "Doe",
    "Email": "john.doe@example.com",
    "Phone": "9876543210"
}

# Step 4: Send POST request
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

response = requests.post(create_contact_url, headers=headers, json=contact_data)

# Step 5: Handle the response
if response.status_code == 201:
    print("✅ Contact created successfully.")
    print("Salesforce ID:", response.json()["id"])
else:
    print("❌ Failed to create contact.")
    print("Status Code:", response.status_code)
    print("Response:", response.json())

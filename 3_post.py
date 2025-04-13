import requests

#Salesforce credentials and details
client_id = '3MVG9RGN2EqkAxhJt87833HHAcRHLDJ0Lj610OHkJ5ppruBFp78kJ8YQrVqfhlf80jL6_0cyeCuSDU663lwXL'
client_secret = '2FE496A913C43CCB4797435DCB98C1D27E333505DDF827A934A29942B49FC596'
redirect_uri = 'http://localhost:8080/callback'

# Updated values
authorization_code = 'aPrxKFKmV5zh2NbmHi9dZiETTZBb6but31hvWH9Mxd_6sM9DiJKWEAClGoByk2UMUV1S.BLALA=='
code_verifier = '4dQ1jz-h9QtevHJoqCZmfBh9v1pOJU3BlvI1r1j-F2o'  # Can be Changed

# Salesforce token endpoint
token_url = 'https://login.salesforce.com/services/oauth2/token'

# Parameters for the POST request
payload = {
    'grant_type': 'authorization_code',
    'code': authorization_code,
    'client_id': client_id,
    'client_secret': client_secret,
    'redirect_uri': redirect_uri,
    'code_verifier': code_verifier
}

# Make the POST request to exchange the authorization code for an access token
response = requests.post(token_url, data=payload)

# Code to Check if the request was successful
if response.status_code == 200:
    token_data = response.json()
    print(f"Access Token: {token_data.get('access_token')}")
    print(f"Instance URL: {token_data.get('instance_url')}")
    print(f"Refresh Token: {token_data.get('refresh_token')}")
else:
    print(f"Error: {response.status_code}")
    print(f"Error Details: {response.text}")

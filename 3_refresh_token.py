# refresh_token.py
import requests

client_id = 'Consumer Key'
client_secret = 'Consumer Secret'
refresh_token = '5Aep8613ZgLngA1wD2JtG0vbH5MTp2GdtPePf9HrPjtYESki3WgNFJWArTVtwv5E_AhBRp446wk_b0B7NMK5e1Z'

token_url = 'https://login.salesforce.com/services/oauth2/token'

payload = {
    'grant_type': 'refresh_token',
    'client_id': client_id,
    'client_secret': client_secret,
    'refresh_token': refresh_token
}

response = requests.post(token_url, data=payload)

if response.status_code == 200:
    token_data = response.json()
    access_token = token_data['access_token']
    instance_url = token_data['instance_url']
    
    # Save access token to a file
    with open('token.txt', 'w') as f:
        f.write(f"{access_token}\n{instance_url}")
    
    print("✅ Access token saved to token.txt")
else:
    print("❌ Error:", response.status_code)
    print(response.text)

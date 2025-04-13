with open('token.txt', 'w') as f:
    f.write(access_token + '\n')
    f.write(instance_url + '\n')
    if refresh_token:
        f.write(refresh_token + '\n')
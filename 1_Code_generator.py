import base64
import hashlib
import os

# Generating the Code Challenger and Code Verifier
code_verifier = base64.urlsafe_b64encode(os.urandom(32)).decode('utf-8').rstrip("=")
code_challenge = base64.urlsafe_b64encode(hashlib.sha256(code_verifier.encode()).digest()).decode('utf-8').rstrip("=")

print(f"Code Verifier: {code_verifier}")
print(f"Code Challenge: {code_challenge}")

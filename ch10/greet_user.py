import json

filename = 'username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcombe back, {username}")
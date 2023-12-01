import json

username = input("what is your name? ")

filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"we'll remember you when you come back, {username}")


##combine remember me file and greet user fi9le into one - when someone runs remember me we want to retrieve their username from memory 

import json 
# load the username, if it has been stored properly 
# otherwise, prompt for the username and store it 

filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your username")
    with open(filename , 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}")
else:
    print(f"welcome back, {username}")

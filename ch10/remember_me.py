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


##Refactoring: process of improving code by breaking it up into a series of functions that have a specific job 

import json
def get_stored_username():
    """Get stored username if available """
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():
    """prompt for a new username"""
    username = input("What is your name")
    filename = 'username.json'
    with open(filename, 'w') as f: 
        json.dump(username, f)
    return username

def greetUser(): 
    """greet the user by name"""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}")
get_new_username() 
get_stored_username()

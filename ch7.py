#User Input and While loops

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please type in your name: ")
print(f"\nHello, {name}")

prompt = "If you tell us who you are, we can personalize the message you see. "
prompt += "\nWhat is your first name? " ## += takes the string that was assigned to prompt and adds the new string onto the end

name = input(prompt)
print(f"\nHello, {name}")

##when using input() it only returns in string - trying using int() to accept numerical input 

prompt = "what is your age? "
prompt += "\nPlease input your age: "
age = input(prompt)
age = int(age)
print(age)
age >= 18


height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48: 
    print("\nYou're tall enough to ride!")
else:
    print("\nYou're not tall enough to ride.")
    
##Modulo Operator - (%) divides one number by another number and returns the remainder: 

5%3

6%3
    
##determine if a number is even or odd

number = input("Enter a number and I will determine if it is even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even")
else: 
    print(f"\nThe number {number} is odd")
    
    
##practice
temp = "what kind of rental would you like? "
car = input(temp)
print(f"\nI'll see if we can find a {car}")

number = input("How many people are in their dinner group? ")
number = int(number)

if number > 8:
    print("\nYou'll have to wait for a table")
else:
    print("\nYour table is ready")

isMultiple = input("please input a number and I will tell if it is a multiple of 10 or not: ")
isMultiple = int(isMultiple)

if isMultiple % 10 == 0:
    print(f"\nThe number {isMultiple} is a multiple of 10")
else:
    print(f"\nThe number {isMultiple} is not a multiple of 10")



##Introducing while Loops: for loop takes a collection of items and executes a block of code once for each item in the collection
## The while loop runs as long as, or while, a certain condition is true 

current_number = 1
while current_number <=10: 
    print(current_number)
    current_number += 2
    

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program: "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
    
## how to get rid of program printing out the word 'quit' as if it were an actual message 

current_number = 1
while current_number <=10: 
    print(current_number)
    current_number += 2
    

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program: "

message = ""
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
        print(message)
        

##Flag : you can devine one variable that determines whether or not the entire program is active. -> acts as a signal to the program 

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program: "

#active represents the flag 

active = True 
while active: 
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)
        
##break statement directs the flow of your program; you can use it to control which lines of code are executed and which aren't so the program only executes code that you want it to, when you want it to 
        
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished )"

while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}")
        
#Using Continue in a loop - Instead of breaking out of a loop entirely without executing the rest of its code, you can use the continue statement to return to the beginning of the loop

current_number = 0
while current_number < 10: 
    current_number += 1
    if current_number % 2 == 0:
        continue
    
    print(current_number)

##Try yourself 


##
prompt = "Tell me a pizza topping, and I will add it to your pizza: "
prompt += "\n(Enter 'quit' when you are finished )"

while True:
    topping = input(prompt)
    
    if topping == 'quit':
        break
    else:
        print(f"{topping.title()} will be added to your pizza")
        

prompt = "The movie theater charges different ticket prices based on your age: "
prompt += "\n(Enter 'quit' when you are done inputting)"

question = "what is your age"

while True:
    age = input(question)
    age = int(age)
    
    if age == 'quit':
        break
    elif age < 3:
        print("The ticket is free")
    elif age > 3 and age < 12:
        print("The ticket is $10")
    else:
        print("The ticket is $15")

## Using a while loop with lists and dictionaries 

#Start with users that need to be verified and an empty list to hold confirmed users 

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

#verify each user until there are no more unconfirmed users - move each verified user into the list of confiremd user s 

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"\nVerifying user: {current_user.title()}")
    confirmed_users.append(current_user)
    
    #display all confirmed users
    print("\nThe following users have been confirmed: ")
    for confirmed_user in confirmed_users: 
        print(confirmed_user.title())
        
        
## Removing all instances of Specific Values from a list: 
# to remove all instances of a value you can run a while loop until value is no longer in the list 


pets = ['dog', 'cat','dog','goldfish','cat','rabbit', 'cat']
print(pets)

while 'cat' in pets: 
    pets.remove('cat')
    
print(pets)

##Filling a dictionary with User Input 
responses = {}

#set a flag to indicate that polling is active 

polling_active = True 

while polling_active:
    #prompt for the person's name and repsonse
    name = input("\nWhat is your name? ")
    response = input("Which mountatin would you like to climb someday?")
    
    #store the response in the dictionary 
    responses[name] = response 
    
    #find out if anyone else is going to take the poll
    repeat = input("would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
        
#polling is complete. show the results
print("\n--- Poll Results ----")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
    
##Try it yourself 

sandwich_orders = ['Philly','BLT','Sausage','Italian']
print(sandwich_orders)
finished_sandwiches = [] 


while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich.title()} sandwich")
    finished_sandwiches.append(current_sandwich)
    
print(f"\nThe follwing sandwiches have been made: ")
for current_sandwich in finished_sandwiches:
    print(current_sandwich.title())
    
##Continue with no pastrami 
sandwich_orders = ['Philly','pastrami', 'BLT','Sausage','pastrami','Italian','pastrami']
print(sandwich_orders)
finished_sandwiches = [] 
print('We have unfortunately run out of pastrami')


while 'pastrami' in sandwich_orders:
     sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich.title()} sandwich")
    finished_sandwiches.append(current_sandwich)
    
print(f"\nThe follwing sandwiches have been made: ")
for current_sandwich in finished_sandwiches:
    print(current_sandwich.title())


##Try it yourself - Dream Vacation 

answer = {}

polling_active = True 

while polling_active:
    name = input("what is your name?")
    location = input("If you could visit one place in the world, where would you go? ")
    
    answer[name] = location
    
    repeat = input("Would you like anyone else to take this poll? (Yes/No)")
    if repeat == 'no':
        polling_active = False
        
print("\n-----Poll Results------")
for name, location in answer.items():
    print(f"{name} would like to travel to {location}")
    
    
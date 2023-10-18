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


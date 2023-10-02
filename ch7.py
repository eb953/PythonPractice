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



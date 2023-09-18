##If Statements 
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
        
## Conditional tests using equality operator

car = 'audi'
car == 'bmw'

car = 'audi'
car == 'audi'


##numerical comparisons 
answer = 17
if answer != 42: 
    print("THat is not the correct answer. Please try again")
    

age = 19 
age < 21

age = 19
age <= 21

age > 21

age > 30

age_0 = 15
age_1 = 18
age_0 >=21 and age_1 >= 21

age_1 = 22
age_0 >= 21 and age_1 >= 21

age_0 = 15
age_1 = 18
age_0 >= 21 or age_1 >= 21

##Check whether value is in list or not 

pizza_toppings = ['pepporoni', 'pineapples', 'chicken']
'pepporoni' in pizza_toppings

pizza_toppings = ['pepporoni', 'pineapples', 'chicken']
topping = 'beef'

if topping not in pizza_toppings:
    print(f"{topping.title()}, is not in the pizza topping list") 


car = 'ford'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audit? I predict False")
print(car=='audi')

age = 12
if age >= 18:
    print("You are old enough to vote")
    print("have you registered to vote?")
elif age > 15 and age < 18:
    print("You are almost there to vote")
else:
    print("You are not old enough to vote")



age = 61
if age <= 4:
    price = 0
elif age > 4 and age < 18:
    price = 25
elif age > 60:
    price = 10
else: 
    price = 40 
    
print(f"Your admission price is ${price}.")

requested_topping = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_topping: 
    print("Adding mushrooms")
if 'extra cheese' in requested_topping:
    print("Adding extra cheese")
if 'pepperoni' in requested_topping:
    print("Adding pepperoni")
    
print("\nFinished making your pizza!")


## test if statement 

##pass
alien_color = ['green', 'yellow', 'red']

if 'green' in alien_color:
    print("The player has earned 5 points!")


#fail
alien_color = ['green', 'yellow', 'red']

if 'orange' in alien_color:
    print("The player has earned 5 points!")
else:
    print("The player gained 0 points")
    
#Alien colors 2 if else

alien_color = ['green', 'yellow', 'red']

if 'orange' in alien_color:
    print("The player has earned 5 points for shooting the alien!")
else:
    print("The player has earned 10 points")
    
#elif

alien_color = ['green', 'yellow', 'red']

if 'orange' in alien_color:
    print("The player has earned 5 points for shooting the alien!")
elif 'blue' in alien_color: 
    print("The player has earned 10 points")
elif 'red' in alien_color:
    print("The player has earned 15 points")
    
#age

age = 69
if age < 2:
    print("This person is a baby")
elif age >= 2 and age < 4:
    print("This person is a toddler")
elif age >= 4 and age < 13:
    print("This person is a kid")
elif age >= 13 and age < 20:
    print("This person is a teenager")
elif age >= 20 and age < 65:
    print("This person is an adult")
elif age >= 65:
    print("this person is an elder")

#for loop:
requested_topping = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_topping:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza")


#how can we add an if statement:

requested_topping = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_topping:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers")
    else: 
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza")

#check empty list
requested_toppings = ['cheese', 'sausage']

if requested_toppings:
    for requested_toppings in requested_toppings:
        print(f"Adding {requested_toppings}")
    print("\nFinished making your pizza")
else:
    print("are you sure you want a plain pizza?")
    
    
available_topping = ['cheese', 'pepperoni', 'anchovies', 'olives', 'artichoke', 'sausage', 'pineapple']
requested_topping = ['pepperoni', 'sausage', 'bbq']

for requested_topping in requested_topping:
    if requested_topping in available_topping:
        print(f"Adding {requested_topping}")
else:
    print(f"Sorry, we don't have {requested_topping}")
    
print("\nFinished making your pizza")

#practice:

user = ['admin', 'jaden', 'eric', 'max', 'will']
for user in user: 
    if 'admin' in user:
        print("Hello admin, would you like to see a status report")
    else:
        print(f"Hello {user}, thank you for logging in again")
        

#check users:
current_users = ['Eric', 'Nathan','Brad','John']
new_users = ['Eric', 'Max', 'Will']

for new_users in new_users:
    if new_users in current_users:
        print(f"The username, {new_users}, is already being used")
    else:
        print(f"{new_users}, is an available username")
        
print("\nFinished making your username")


#ordinal numbers
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for numbers in numbers: 
    if '1' in numbers:
        print(f"{numbers}st")
    elif '2' in numbers:
        print(f"{numbers}nd")
    elif '3' in numbers:
        print(f"{numbers}rd")
    else:
        print(f"{numbers}th")
        
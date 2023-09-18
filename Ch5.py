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
    


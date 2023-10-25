##Functions 

##blocks of code that are designed to do one specific job 

##store functions in separate files called "modules" to help organize your main program files

##def = function definintion -> tells python the name of the funciton and if applicable, what kind of information the function needs to do its job
##three quotation marks """"Word""" is a comment called docstring which describes what the function does 


def greet_user(username): 
    """Display a simple greeting"""
    print(f"Hello, {username.title()}!")
    

greet_user('Eric')

##parameter = a piece of information the function needs to do its job ie. above the parameter needed was 'username'
## Argument = a piece of information that's passed from a function call to a function ie. above the argument was 'Eric' 

##Try it yourself 

def display_message():
    """display a sentence that summarizes what we learn in this chapter
    """
    print("Introduction to chapter 8 is functions")
    
display_message()

def favorite_book(title):
    """Display favorite book
    """
    print(f"my favorite book is {title.title()}.")
    
favorite_book('Art of Decay')

##Passing Arguments

##Because a function defintion can have multiple parameters, a function call may need multiple arguments
##Positional arguments - need to be in the same order the paramters were written 
##Keyword arguments - each argument consists of a variable name and a value and lists and dictionaries of values 


#Positional argument ex

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet('hamster','harry')


##Multiple function cells

pet_type = []
name_list = []

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    
    for i in (animal_type):
        pet_type.append(animal_type)
        
        
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet('hamster','harry')
describe_pet('dog','willie')

print(pet_type)

#for above attempting to add arguments into list 

## Order Matters in a positional argument 

# don't switch arguments describe_pet('hamster', 'harry') and describe_pet('harry', 'hamster')

##Keyword Arguments - a name value pair that you pass to a function -> free you from having to worry about correctly ordering your arguments in the function call and they clarify the role of each value in the function call. 

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet(animal_type='hamster',pet_name='harry')


#default values - if an argument for a parameter is provided in the function call, python uses the argument value. if not it uses the parameters default value 
#When you use default values, any parameter with a default value needs to be listed after all the parameters that don't have defaulrt values. This allows python to continue interpreting postional arguments correctly 


def describe_pet(pet_name, animal_type = 'dog'):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet('Eric') 


##Try it yourself 


def make_shirt(text, shirt_size = 'medium'): 
    """Display Information about shirt"""
    print(f"\nThe size of my shirt is {shirt_size}.")
    print(f"My shirt reads, {text}")
    
make_shirt('I love New York') 


def describe_city(city_name, country='Iceland'):
    """Display information about location"""
    print(f"\n{city_name.title()} is in {country.title()}.")
    
describe_city('New York', country='USA')

##Return Vlaues - the value a function returns is called a return value. The return statement takes a value from isnide a function and sends it back to the line that called the function. Return values allow yuou to move much of your program's grunt work into functions, which can simplify the body of your program 

def get_formated_name(first_name, last_name):
    """Return a full name, neatly formated"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formated_name('Eric', 'Banavong')
print(musician)

##making an argument optional -> set the parameter to an empty string ('')

def get_formated_name(first_name, last_name, middle_name = ''):
    """return a full name, neatly formated"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else: 
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formated_name(first_name='Eric', middle_name='robert', last_name='Banavong')
print(musician)

def get_formated_name(first_name, last_name, middle_name = ''):
    """return a full name, neatly formated"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else: 
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formated_name(first_name='Eric', last_name='Banavong')
print(musician)

##Returning a dictionary - a function can return any kind of value you need it to - including lists and dictionaries 

def build_person(first_name, last_name): 
    """return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    return person 
musician = build_person('Eric','banavong')
print(musician)

## None evaluates to false unless specified 
def build_person(first_name, last_name, age = None): 
    """return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age']= age
    return person 
musician = build_person('Eric','banavong', age = 25)

## Using a function with a while loop 

## above is an infinite while loop - need to insert a break 

def get_formated_name(first_name, last_name): 
    """return a full name, neatly formated"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True: 
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit )")
    
    f_name = input("first name: ")
    if f_name == 'q':
        break 
    l_name = input ("last name: ")
    if l_name == 'q':
        break 
    formated_name = get_formated_name(f_name, l_name)
    print(f"\nHello, {formated_name}")


##Try it yourself 

def city_country(city, country): 
    full_name = f" {city}, {country}"
    return full_name.title() 
    
while True: 
    print("\nPlease enter a city and country")
    print("(enter 'q' at any time to quit)")
    
    c_name = input("city name: ")
    if c_name == 'q': 
        break 
    country_name= input("country name: ")
    if country_name == 'q':
        break 
    
    print(f"\n{c_name}, {country_name}")
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



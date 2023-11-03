##Classes
# Object-oriented programming -> you write classes that represent real-world things and situations, and you create objects based on these classes. When you write a class, you define the general behavior that a whole category of obejcts can have 
# making an object from a class is called instantiation, and you work with instances of a class 

#Example: Creating and using a class 

class Dog: 
    """A simple attempt to model a dog"""
    
    def __init__(self, name, age):
        """initialize name and age attribute"""
        self.name = name
        self.age = age
        
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self): 
        """Simulate rolling voer in response to a command"""
        print(f"{self.name} rolled over!")
        
        
my_dog = Dog('willie', 6)
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")

my_dog.sit()
my_dog.roll_over()

        
## __Init__() method 
## a function that is part of a class is a method -> init method is a special method that python runs automatically whenever we create a new instance based on the class. in reference to above, self is required in the method definition and it must come first before the other parameters. When python calls this method later(to create an instance of dog) the method call will automatically pass the self arguement. Every method call associated with an instance automatically passes self, whcih is a reference to the instance itself. IT GIVES THE INDIVIDUAL INSTANCE ACCESS TO THE ATTRIBUTES AND METHODS IN THE CLASS. ie name and age 

## Making an Instance from a Class 
# Think of a class as a set of instructions for how to make an instance 

my_dog = Dog('Max', 25)
your_dog = Dog('Will', 24)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog's age is {your_dog.age}")
my_dog.sit()

print(f"Your dog's name is {your_dog.name}")
print(f"Your dog's age is {your_dog.age}")
your_dog.sit() 


##Try it yourself 

class Restaurant: 
    """Model a restuarant"""
    def __init__(self, restaurant_name, cuisine_type): 
        self.restaurant_name = restaurant_name
        self.cusine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"The restaurant is called {self.restaurant_name}.")
        
    def open_restaurant(self):
        print(f"\nThe restaurant is open and will be serving {self.cusine_type}.")
        
my_restaurant = Restaurant('Jones', 'Italian')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant = Restaurant('Jones', 'Italian')
Eric_restaurant = Restaurant('Boiling Point', 'Seafood')
Frida_restaurant = Restaurant('Frida', 'Hispanic')

Frida_restaurant.open_restaurant()
Eric_restaurant.describe_restaurant()


class User: 
    
    def __init__(self, first_name, last_name, age, sex, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex 
        self.location = location 
    
    def describe_user(self):
        print(f"\nThe user's name is {self.first_name} {self.last_name}. ")
        print(f"\n{self.first_name} {self.last_name} is {self.age} years old")
        print(f"\n{self.first_name} {self.last_name} is {self.sex} and lives in {self.location}")
    
    def greet_user(self):
        print(f"\nWe would like to extend a warm welcome to {self.first_name} {self.last_name}")
    
    
Eric_B = User('Eric', 'Banavong', 25, 'Male', 'Los Angeles')
Eric_B.describe_user()
Eric_B.greet_user() 

Frida_P = User('Frida', 'Pena', 24, 'Female', 'Pomona')
Frida_P.describe_user()
Frida_P.greet_user()

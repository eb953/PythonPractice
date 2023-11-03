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
        print(f"{self.age} rolled over!")
        
## __Init__() method 
## a function that is part of a class is a method -> init method is a special method that python runs automatically whenever we create a new instance based on the class. in reference to above, self is required in the method definition and it must come first before the other parameters. When python calls this method later(to create an instance of dog) the method call will automatically pass the self arguement. Every method call associated with an instance automatically passes self, whcih is a ference to the instance itself. IT GIVES THE INDIVIDUAL INSTANCE ACCESS TO THE ATTRIBUTES AND METHODS IN THE CLASS. ie name and age 


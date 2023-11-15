"""A class that can be used to represent a car"""

class Car:
    """Represent a car"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year  
        self.odometer_reading = 0 
        self.gas_tank = 100
    def get_descriptive_name(self):
        """return a formatted descriptive name"""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()
    
    def read_odometer(self):
        """print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it")
        
    def update_odometer(self, mileage): ## adding method to update certain attributes 
        """Set the odometer reading to the given value. Reject the change if it attempts to roll the odometer back"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage 
        else:
            print("You can't roll back an odometer")
    
    def increment_odometer(self, miles):
        """add the given amount to the odometer reading"""
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        print(f"The gas tank is now set to {self.gas_tank}")
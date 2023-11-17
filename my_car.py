from car import Car, ElectricCar

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_tesla = ElectricCar('Tesla', 'S', 2023)

print(my_tesla.get_descriptive_name())
my_new_car.odometer_reading= 23
my_new_car.read_odometer() 


## The import statement at 1 tells python to open the car module and import the class Car. 
## You can import a module into a module 
#From car import Car
#From electric_car import ElectricCar 


##Aliases 
# -> from electric_car import ElectricCar as EC 
# my_tesla = EC('tesla', 'roadster', 2019)


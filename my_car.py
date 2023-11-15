from car import Car 

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading= 23
my_new_car.read_odometer() 


## The import statement at 1 tells python to open the car module and import the class Car. 
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

# no longer case sensitive 
car = 'Audi'
car.lower() =='audi'
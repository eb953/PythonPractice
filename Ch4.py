## Loops 

magicians = ['eric', 'max','will', 'parker']
for x in magicians:
    print(x)

## x is the variable - better to use singluar and plural names -> magician in magicians 


magicians = ['eric', 'max','will', 'parker']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!"
    )

## adding a second line

magicians = ['eric', 'max','will', 'parker']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!"
    )
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

## ending loop and adding final message 

magicians = ['eric', 'max','will', 'parker']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!"
    )
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great show!")


## Try with pizza 

pizzas = ['pepperoni', 'cheese', 'artichoke']
for pizza in pizzas: 
        print(f"{pizza.title()}, is the best type of pizza!")
        print(f"I would always choose, {pizza.title()}, as my go to pizza. \n")
print("No matter what, I'll always love pizza")

## Try wit animals 

animals = ['dogs', 'cats', 'hamsters',]
for animal in animals:
        print(f"{animal.title()}, are known as household pets")
        print(f"This animal is also part of the mammal class \n")
print("Any of these animals would make a great pet!")

## range to generate a series of numbers

for value in range(1,6):
    print(value)

## create list of numbers using range 
numbers = list(range(1,6))
print(numbers)

## skip numbers 

even_numbers = list(range(2,11,2))
print(even_numbers)

## more numbers 
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)

## shorten syntax, remove temporary variable 

squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares) 

## list comprehensions 

squares = [value ** 2 for value in range(1,11)]
print(squares)


## Try excercise 

#print counting to 20 
for value in range(1,21):
    print(value)

# make a list from 1 to 1 million
big_numbers = list(range(1,1000001))
print(big_numbers)

min(big_numbers)
max(big_numbers)
sum(big_numbers)

# odd number list 
odd_numbers = list(range(1,21,2))
for odd_number in odd_numbers:
    print(odd_number)

# threes
triples = list(range(3,30,3))
for triple in triples:
    print(triple)

# cubes - make sure to create empty list first 
numbers = []
for values in range(1,11):
    numbers.append(values ** 3)
print(numbers)

# try list comprehension
numbers = [value**3 for value in range(1,11)]
print(numbers)


## slicing a list - specify the first and last elements that wants to be worked with
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])

## looping through a slice 

players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[:5]:
    print(player.title())

## copying a list 

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

## use append to add to copy list 

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)


## Try it yourself 

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("\nThe first three items in the list are:")
print(players[0:3])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("\nThe middle three items in the list are:")
print(players[1:4])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("\nThe last three items in the list are:")
print(players[2:5])


my_pizzas = ['cheese', 'artichoke', 'crab']
friend_pizzas = my_pizzas[:]

my_pizzas.append('margherita')
friend_pizzas.append('bbq')

print("\nMy faborite pizzas are:")
print(my_pizzas)

print("\nMy friend's favorite pizzas are:")
print(friend_pizzas)

for my_pizza in my_pizzas:
    print("\nMy faborite pizzas are:")
    print(my_pizzas)

for friend_pizza in friend_pizzas:
    print("\nMy friend's favorite pizzas are:")
    print(friend_pizzas)

## Tuples = immutable, a list of items that cannot change - can define them by using set of paranthesis versus brackets 

dimensions = (220,50)
print(dimensions[0])
print(dimensions[1])

## looping through all values in a tuple
dimensions = (220,50)
for dimension in dimensions: 
    print(dimension)

dimensions = (220,50)
print("Original dimensions:")
for dimension in dimensions: 
    print(dimension)

dimensions = (400,98)
print("\nModified dimensions:")
for dimension in dimensions: 
    print(dimension)


## Try it with buffet 
buffet_foods = ('crab', 'pizza', 'ice cream', 'salad', 'steak')
print("buffet style food:")
for buffet_food in buffet_foods:
    print(buffet_food)

##try modify tuple - will produce error 
buffet_foods[0] = 'chicken'

## modify tuple by rewriting tuple 
buffet_foods = ('crab', 'pizza', 'ice cream', 'salad', 'steak')
print("buffet style food:")
for buffet_food in buffet_foods:
    print(buffet_food)

buffet_foods = ('crab', 'pizza', 'ice cream', 'porkchops', 'chicken')
print("\nupdated buffet style food:")
for buffet_food in buffet_foods:
    print(buffet_food)








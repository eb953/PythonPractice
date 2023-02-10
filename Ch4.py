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

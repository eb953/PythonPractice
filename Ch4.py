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


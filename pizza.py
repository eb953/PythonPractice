##test out modules 

def make_pizza(size, *toppings):
    """list out size and topping of pizza"""
    print(f"\nThe size of the pizza is {size} and the following toppings added: ")
    for topping in toppings:
        print(f" - {topping}")

print("give me two numbers, and I'll add them")
print("Enter 'q' to quit")

while True:
    first_number = input("What is the first number: ")
    if first_number == 'q':
        break 
    second_number = input("What is the second number: ")
    if second_number == 'q': 
        break 
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("One of the values inputed is not a number")
    print(answer)
    

## add pass 

print("give me two numbers, and I'll add them")
print("Enter 'q' to quit")

while True:
    first_number = input("What is the first number: ")
    if first_number == 'q':
        break 
    second_number = input("What is the second number: ")
    if second_number == 'q': 
        break 
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        pass
    print(answer)

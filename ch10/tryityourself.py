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

    ##Cats and Dogs 10-8

with open ('cats.txt', 'w') as c:
    c.write("Tokyo\n")
    c.write("snowy\n")
    c.write("smokey\n")

with open('dogs.txt', 'w') as d:
    d.write("cinammon\n")
    d.write("bailey\n")
    d.write("blue\n")

##
def printFiles(filename):
    """open and read files"""
    try:
        with open(filename, 'r') as f:
            contents = f.read()
    except FileNotFoundError:
        print("The file does not exist!")

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    printFiles(filename) 
##above is incorrect 

##below is answer
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print(f"\nReading file: {filename}")
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print("  Sorry, I can't find that file.")


with open('pi_digits.txt') as file_object: 
    contents = file_object.read() 
print(contents.rstrip())

##The open() functiion needs one argument: the name of the file you want to open -> 'pi_digits.txt' 
##returns an object representing pi_digits.txt -> assigns to file_objet 

##rstrip() removes extra blank line after the return 


#File Paths 

## Relative file paths tell Python to look for a given location relative to the directory where the currently running program file is stored

## ex: with open('text_files/filename.txt') as file_object: 

filename = 'pi_digits.txt'

with open(filename) as file_object: 
    for line in file_object:
        print(line.rstrip())

##Reading line by line 

##Making a list of lines from a file 

filename = 'pi_digits.txt'

with open (filename) as file_object: 
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# Readlines() method takes each line from the file and stores it in a list. This list is then assigned to lines, which we can continue to work with after the with block ends. the for loop will print each line from lines. because each item in liens corresponds to each line in the file, the output matches the contents of the file exactly 


#Working with a file's content

filename = 'pi_digits.txt'

with open (filename) as file_object: 
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# at pi_string we create a variable to hold the digits of pi 
# we then create a loop that adds each line of digits to pi_string and remvoes the newlin character from each line 
# we then print the string and also print how long the string is 

## Note: when python reads a text file it interprets all text in the file as a string. to read in a number you need to convert it to an interger using the int() function or convert it to a float using the float() function

for line in lines:
    pi_string += line.strip() 

birthday = input("Enter birthday in the format: mmddyy")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi ")
else:
    print("Your birthday does not appear in the first million digits of pi")



filename = 'learning_python.txt'
with open(filename) as file_object: 
    content = file_object.read() 
    print(content.strip())


#For loop -> write a program that reads the file and prints what you wrote 3 times 
filename = 'learning_python.txt'
with open(filename) as file_object: 
    for line in file_object: 
        print(line.rstrip())

## storing the lines in a list then work outside of with block 

filename = 'learning_python.txt'

with open(filename) as f: 
    contents = f.readlines()

for content in contents:
    print(content.rstrip())


## 
message = "I really like dogs"
message.replace('dog', 'cat')

##Writing to an empty file

filename = 'programming.txt'

with open(filename, 'w') as file_object: 
    file_object.write("I love programming. \n")
    file_object.write("I love creating neew games. \n")

#when adding multiple lines the string will squish together so adding \n helps 

#open() in the above example has 2 arguments. The first argument is still the name of the file we want to open. The second argument 'w' tells python that we want to open the file in WRITE mode. You can open a file in read mode ('r') write mode ('w') and append mode ('a') or a mode that allows you to read and write ('r+') If you omit the mode argument Python opens the file in read only mode by default. Be careful!! If open the file in write mode and there is already content in it, it will erase everything before returning the new edits

#appending will open and add to a file without erasing and replacing the contents 

filename = 'programming.txt'

with open(filename, 'a') as file_object: 
    file_object.write("I also love finding meaning in dew datasets. \n")
    file_object.write("I creating new apps and running it in a broswer. \n")

##Try it yourself 


User = input("What is your name: ")
filename = 'guest.txt'
with open(filename, 'w') as file_object:
    file_object.write(f"{User} \n")

##Try it yourself

filename = 'guest_book.txt'
print("Enter 'quit' when you are finished")

while True: 
    name = input("\nWhat is your name")
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"{name}\n")
        print(f"Hi, {name}, you've been added to the guest book")

##Try it yourself 10-5

filename = 'poll.txt'
print("Enter 'quit' when you are finished")

reasons =[]
while True: 
    name = input("\nWhat is your name")
    if name == 'quit':
        break 
    elif name != 'quit': 
        reasons.append(name)
        reason = input(f"{name}, why do you like programming?\n")
        reasons.append(reason)
        
with open(filename, 'a') as file_object: 
    for reason in reasons:
        file_object.write(f"{name}, your recorded resonse is {reason}\n")
## does not work :(




filename = 'programming_poll.txt'

responses = []
while True:
    response = input("\nWhy do you like programming? ")
    responses.append(response)

    continue_poll = input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != 'y':
        break

with open(filename, 'a') as f:
    for response in responses:
        f.write(f"{response}\n")
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
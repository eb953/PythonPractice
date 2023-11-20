with open('pi_digits.txt') as file_object: 
    contents = file_object.read() 
print(contents.rstrip())

##The open() functiion needs one argument: the name of the file you want to open -> 'pi_digits.txt' 
##returns an object representing pi_digits.txt -> assigns to file_objet 
##rstrip() removes extra blank line after the return 


#File Paths 

## Relative file paths tell Python to look for a given location relative to the directory where the currently running program file is stored

## ex: with open('text_files/filename.txt') as file_object: 


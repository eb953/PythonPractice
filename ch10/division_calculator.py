##Exceptions: whenever an error occurs that makes Python unsure what to do next, it creates an exception object. A try-except block asks Python to do something but it also tels python what to do if an exception is raised

print(5/0)
##ZeroDivisionError: division by zero is an exception object 

##Using try-except block

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")


print("give me two numbers, and I'll divide them")
print("Enter 'q' to quit")

while True: 
    first_number = input("\nfirst number: ")
    if first_number == 'q':
        break 
    second_number = input("\nsecond number:")
    if second_number == 'q':
        break 
    answer = int(first_number)/ int(second_number)
    print(answer)
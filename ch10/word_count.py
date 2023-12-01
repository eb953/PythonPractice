def count_words(filename):
    """Count the approximate number of words in a file"""
    try:
        with open(filename, encoding='utf-8') as f:
         contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words")

filenames = ['alice.txt','pattern.txt','russian.txt']
for filename in filenames:
   count_words(filename)

##Failing Silently 
# You can add pass in in the try else block and Python will continue running despite errors 


def count_words(filename):
    """Count the approximate number of words in a file"""
    try:
        with open(filename, encoding='utf-8') as f:
         contents = f.read()
    except FileNotFoundError:
        pass ## will continue running despite file not found 
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words")

filenames = ['alice.txt','pattern.txt','russian.txt', 'adobe.txt']
for filename in filenames:
   count_words(filename)
    

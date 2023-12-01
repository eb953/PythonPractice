##Json - the json module allows you to dump simple python data structures into a file and load the data from that file the next time the program runs 

import json
numbers = [2,3,5,7,11,13]

filename = 'numbers.json'
with open (filename, 'w') as f:
    json.dump(numbers, f)
##above will dump the data into a json file 


import json

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)
    
print (numbers)

##above will load and read out the json file 
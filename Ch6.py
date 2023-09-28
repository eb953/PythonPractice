## dictionaries 

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

alien_0['x_position'] = 0 
alien_0['y_position'] = 25

print(alien_0)


##starting with an empty dictionary 
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

##modifying values in a dictionary
alien_0['color'] = 'green'
print(f"The alien is currently {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")


alien_0 = {'x_position': 1 , 'y_position': 25, 'speed': 'medium'}
print(f"Original Position: {alien_0['x_position']}")

##move the alien to the right
#Detemrine how far to move the alien based on its current speed

if alien_0['speed'] == 'slow': 
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

#the new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"The new alien position is {alien_0['x_position']}")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

#Dictionary of similar objects 
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }   

language = favorite_languages['sarah'].title() 
print(f"Sarah's favorite language {language}")


##test
Wooster = {
    'first_name': 'Eric',
    'last_name': 'Banavong',
    'age': 25,
    }
print(Wooster)
print(f"The person's first name that lives in wooster is {Wooster['first_name']}")
print(f"The person's last name that lives in wooster is {Wooster['last_name']}")
print(f"The person's age that lives in wooster is {Wooster['age']}")





for name, value in Wooster.items():
    print(f"\nName: {name}")
    print(f"Value: {value}")
    
    
    
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

#if 'erin' not in favorite_languages.keys():
       # print("Erin, please take our poll!")

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends: 
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
    




##keys() method returns a list of keys without their values ie. favorite_languages.keys() 
#values() method returns a list of values without their keys   ie. favorite_languages.values()     
## A set is a collection in which each item must be unique 

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
    
    
##Rivers

Major_Rivers = {
    'nile': 'egypt',
    'Rio Grande': 'mexico',
    'Chang': 'china',
    'Amazon': 'brazil',
    }
for river in Major_Rivers.values():
    print(river.title())


##for river, country in Major_Rivers.items():
    ##print(f"The {river.title()} is a river that runs through this country, {country.title()} ")
    
    
    
##nesting - store multiple dictionaries in a list, or a list of items as a value in a dictionary 
    #Range() returns a series of numbers 
    
    
#nesting example

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)

#use range to create 30 aliens 

aliens = []

for alien_number in range(30):
    new_alien = {'color':'green','points':5, 'speed': 'slow'}
    aliens.append(new_alien)
    
for alien in aliens[:5]:
    print(alien)
print("...")

print(f"Total number of aliens: {len(aliens)}")

##Change the first 3 aliens to yellow, medium-speed aliens worth 10 points each 

aliens = []

for alien_number in range(30):
    new_alien = {'color':'green','points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    
for alien in aliens[0:3]:
    if alien['color'] == 'green':
            alien['color'] ='yellow'
            alien['speed'] ='medium'
            alien['points'] = 10
    elif alien['color'] == 'yellow':
            alien['color'] = 'red'
            alien['speed']= 'fast'
            alient['points'] = 15     
            
for alien in aliens[:5]:  
    print(alien)
print("...")

print(f"Total number of aliens: {len(aliens)}")



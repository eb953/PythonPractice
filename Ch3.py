#Lists 

# Index positions start at 0
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0].title())
message = f"My first bicycle was a {bicycles[2].title()}"
print(message)

#try myself

friends = ['shey', 'max', 'will', 'parker']
print(friends)

messageA = f"My friend {friends[0].title()} is from Guetamala"
messageB = f"There is a friend named {friends[1].title()} who is from England"
messageC = f"{friends[2].title()} was raised in Yorba Linda"
messageD = f"A midwestern boy is something {friends[3].title()} would be considered as"

print(messageA)
print(messageB)
print(messageC)
print(messageD)

## sort and reverse 
cars = ['bmw', 'audi', 'toyota', 'honda']
print(cars)
cars.reverse()
print(cars)
cars.sort()
print(cars)


##sorted method, finding length 
cars = ['bmw', 'audi', 'toyota', 'honda']
print(cars)

print("\n Here is the sorted list:")
print(sorted(cars))

print("\n Here is the origial list:")
print(cars)

len(cars)

##Try it yourself (Worlds)
Worlds = ['Laos', 'Germany', 'Guetamala', 'England', 'Poland']
print(Worlds)



print(sorted(Worlds))

print(" \n printing original")
print(Worlds)


Worlds = ['Laos', 'Germany', 'Guetamala', 'England', 'Poland']
print(sorted(Worlds))

Worlds.reverse()
print(Worlds)

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

#Guest List 

Guests = ['tom', 'bob', 'shelby', 'larry']
messageA = f"{Guests[0].title()}, you have been invited to Eric's dinner."
messageB = f"{Guests[1].title()}, you have been invited to Eric's dinner."
messageC = f"{Guests[2].title()}, you have been invited to Eric's dinner."
messageD = f"{Guests[3].title()}, you have been invited to Eric's dinner."

print(messageA, messageB, messageC, messageD)

#Someone could not make it
Guests = ['tom', 'bob', 'shelby', 'larry']
print(Guests)
print("Larrry could not make it and will be replaced")

Guests[3] = 'mary'
print(Guests)

messageA = f"{Guests[0].title()}, you have been invited to Eric's dinner."
messageB = f"{Guests[1].title()}, you have been invited to Eric's dinner."
messageC = f"{Guests[2].title()}, you have been invited to Eric's dinner."
messageD = f"{Guests[3].title()}, you have been invited to Eric's dinner."

print(messageA, messageB, messageC, messageD)


#Guests for bigger dinner table 
Guests = ['tom', 'bob', 'shelby', 'larry']
print(Guests, "a new dinner table has been made available and so more people can join")

Guests.insert(0, 'pame')
Guests.insert(2, 'nathan')
Guests.append('Lena')

print(Guests)

messageA = f"{Guests[0].title()}, you have been invited to Eric's dinner."
messageB = f"{Guests[1].title()}, you have been invited to Eric's dinner."
messageC = f"{Guests[2].title()}, you have been invited to Eric's dinner."
messageD = f"{Guests[3].title()}, you have been invited to Eric's dinner."
messageE = f"{Guests[4].title()}, you have been invited to Eric's dinner."
messageF = f"{Guests[5].title()}, you have been invited to Eric's dinner."
messageG = f"{Guests[6].title()}, you have been invited to Eric's dinner."

print(messageA)
print(messageB)
print(messageC)
print(messageD)
print(messageE)
print(messageF)
print(messageG)


#pop method 
print(Guests)
print(f"They're can only be 2 people for dinner")

remove_last = Guests.pop()
print(f"Hello {remove_last.title()}, I apologize for the inconvenience but I can no longer fit you in the dinner reservation")

remove_last = Guests.pop()
print(f"Hello {remove_last.title()}, I apologize for the inconvenience but I can no longer fit you in the dinner reservation")

remove_last = Guests.pop()
print(f"Hello {remove_last.title()}, I apologize for the inconvenience but I can no longer fit you in the dinner reservation")

remove_last = Guests.pop()
print(f"Hello {remove_last.title()}, I apologize for the inconvenience but I can no longer fit you in the dinner reservation")

remove_last = Guests.pop()
print(f"Hello {remove_last.title()}, I apologize for the inconvenience but I can no longer fit you in the dinner reservation")

Guests.append('tom')

print(Guests, "you are still invited to the dinner ")

del Guests[0]

print(Guests)




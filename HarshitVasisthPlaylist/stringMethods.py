#len() function
name="Hare Krishna"
# length=name.len() #error

length=len(name)
print(length)

#lower() method
# lower=name.lower("H")  #error

lower=name.lower()
print(lower)

# what if I want to lower just an one char in string ???

charLower=name[0].lower()
print(charLower)

print(name.count('a'))
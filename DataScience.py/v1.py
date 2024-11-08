Name="Krishna"
Age=21
print("Name:{},Age:{}".format(Name,Age))
print(f"Name:{Name},Age:{Age}")
print("Name:%s,Age:%f"%(Name,Age))
print(f"Age:{Age:.2f}")


import math
print(f"valus of pi upto its two decimal {math.pi:.2f}") 

print(Name,end=" ")
print(Age)


print(Name,Age,sep="*")

###### Printing a list ############
hobbies=["reading","hiking","coding","playing"]
print(hobbies) #['reading', 'hiking', 'coding', 'playing']

hobbies.append("Swimming")
print(hobbies)  #['reading', 'hiking', 'coding', 'playing', 'Swimming']


###............ Joining list items into a string..................
print(",".join(hobbies)) #reading,hiking,coding,playing,Swimming


###>>>> Printing a dictionary <<<
person={"name":'Alice',"Age":30}
print(person) #{'name': 'Alice', 'Age': 30}

#>>> Accessing Dictionary Values <<<
print(f"name:{person['name']},Age:{person['Age']}")  #name:Alice,Age:30


##>> Printing a tuple <<<

coordinates=(10,20)
print(coordinates) #(10, 20)

x,y=coordinates
print(f"X:{x},Y:{y}")  #X:10,Y:20

## printing a set ##

fruits={"Apple","PineApple","CustardApple"}
print(fruits)  #{'Apple', 'CustardApple', 'PineApple'}

# Printing escape character
print("Hello\nWorld")


#printing raw string
print(r"Hello\nWorld")   #Hello\nWorld





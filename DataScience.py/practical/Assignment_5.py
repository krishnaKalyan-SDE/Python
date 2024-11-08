list1=[1,2,3,"DSA","Python","Python"]
print(list1)

list1.append("CPP")
print(list1)

list2=list1.copy()
print(list2)

list3=list1.count("Python")
print(list3)

cars=['Ford','BMW','Volvo']
fruits=['apple','banana','cherry']
cars.extend(fruits)
print(cars)

fruits=["mango","custardapple"]
points=(1,4,5,9)
fruits.extend(points)
print(fruits)

number=[4,55,64,32,16,32]
x=number.index(32)
print(x)

pop=list1.pop(1)
print(pop)
print(list1)

fruits.remove("mango")
print(fruits)

list1.reverse()
print(list1)
degree=['DS','BTech','MTech']
degree.sort()
print(degree)



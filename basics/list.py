"""
list1=[]
for i in range(1,6):
    user=input(f"Enter name{i} : ")
    list1.append(user)
   # print(list1)
#o/p:['Yudhistir', 'Bhim', 'Arjun', 'Nahakul', 'Sahadev']


list2=["Sugar","BP","TB","Cough","Fever","weakness"]
print(list2[0],end=" ") 
print(list2[1])
#Sugar BP

list2.clear()
print(list2)    #[]

#create a new list and copy all elements of list2 in x
x=list2.copy()
print(x)   #['Sugar', 'BP', 'TB', 'Cough', 'Fever', 'weakness']


#another way to define list
list=(("Apple","Mango","PIneApple","CustardApple","Chickoo","Pineapple"))
print(list)

print(len(list))

#list.append("Grapes")
#print(list)

count=list.count("Apple")
print(count)

#count no of 9 in this list
list4=[1,2,3,4,9,9,9,0,9,1,9,2,9,3,9,3,9,4,9,49,9,9,9,9]
count=list4.count(9)
print(count)
list4.sort(reverse=False)
print(list4)

#extend means add elements of list6 in list5
list5=[1,3,5,7]
list6=[2,4,6,8]
list5.extend(list6)
print(list5)

"""

list=[1,2,3,4,5]
print(list) #[1, 2, 3, 4, 5]
print(list[1]) #2
print(list[2:4]) #[3, 4]
list[0]="mango"
print(list) #['mango', 2, 3, 4, 5]

list.append("Pineapple")
print(list)
list1=[6,7,8,9,10] #['mango', 2, 3, 4, 5, 'Pineapple']

list.insert(1,"one")
print(list)          #['mango', 'one', 2, 3, 4, 5, 'Pineapple']

list.extend(list1)
print(list)   #['mango', 'one', 2, 3, 4, 5, 'Pineapple', 6, 7, 8, 9, 10]

list.remove("mango")
print(list)   #['one', 2, 3, 4, 5, 'Pineapple', 6, 7, 8, 9, 10]
print(list.pop())  #10
print(list.pop(5))
print(list)

# print(list[::-1])  #[9, 8, 7, 6, 5, 4, 3, 2, 'one']
print(list[-1:-5]) #[]
print(list[-1:-5:-1])


#creating a list of squares
list=[]
for i in range(1,11):
    list.append(i*i)  
print(list)  #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

list2=[x**2 for x in range(1,6)]
print(list2)


even_list=[x for x in range(1,10) if x%2==0]
print(even_list) #[2, 4, 6, 8]


fruits=['apple','mango','banana','pineapple']
print(len(fruits))
fruits.sort()
print(fruits)  #['apple', 'banana', 'mango', 'pineapple']
fruits.reverse()
print(fruits) #['pineapple', 'mango', 'banana', 'apple']
index=fruits.index('banana')
print(index)
count=fruits.count('apple')
print(count)

for fruit in fruits:
    print("Fruits:",fruit)
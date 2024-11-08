list1=[]
for i in range(1,11):
    list1.append(i)
print(list1)

#accessing last element of list
print(list1[len(list1)-1])

#modify the third element of the list
list1[2]="modified"
print(list1)

#add an element to the end of list
list1.append(11)
print(list1)

#remove an element by value from the list
list1.remove(11)
print(list1)

#remove an element by index from the list
list1.pop(2)
print(list1)

# 8.Find the index of an element in a list
print(list1.index(10))

# 9. Reverse the elements in a list
list1.reverse()
print(list1)

# 10. Sort a list of integers in ascending order.
list1.sort()
print(list1)

# 11.Sort a list of strings in alphabetical order.
list11=["zebra","elephant","Zebra"]
list11.sort(key=str.lower) #if you want "Z" after small"z"
print(list11)

# 12. Count the number of times a value appears in a list
list12=[1,2,3,4,4,3,2,1]
ans=list12.count(3)
print(ans)

#13. Extend a list by another list.
list13=["extend","expand"]
list11.extend(list13)
print(list11)

#14.Clear all elements from a list
list1.clear()
print(list1)

#15.Check if an element is in a list
print(list1)

                ###list slicing###
#16.Extract the first three elements of a list.
list13=["Apple","Microsoft","Walmart","PhonePay"]
print(list13[0:3])

#17. Extract the last three elements of a list
print(list13[-3::1])

#18.Extract every second element from a list.
print(list13[0:len(list13)-1:2])

#19. Reverse a list using slicing
print(list13[-1::-1])

list13[2]=[100,101,102]
print(list13)



              ###list Comprehension###
# 26. Create a list of squares of numbers from 1 to 10 using list comprehension.
list26=[i*i for i in range(1,11)]
print(list26)

#28. Create a list of even numbers from 1 to 20 using list comprehension
list28=[i for i in range(1,21) if i%2==0]
print(list28)




my_tuple=("banana","apple","Grapes")
list2=list(my_tuple)
list2[2]="Changed"
my_tuple2=tuple(list2)
print(my_tuple2)


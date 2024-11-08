list=['Mango','Apple','PineApple',1,2,2.5,2.56]
list.append("SGGS")
print(list)
#['Mango', 'Apple', 'PineApple', 1, 2, 2.5, 2.56, 'SGGS']

# list.clear()
# print(list)
# #[]

list1=list.copy()
print(list1)
#['Mango', 'Apple', 'PineApple', 1, 2, 2.5, 2.56, 'SGGS']

print(list.index("Mango"))
#0

list.pop(2)
print(list)
#['Mango', 'Apple', 1, 2, 2.5, 2.56, 'SGGS']

list.reverse()
print(list)
#['SGGS', 2.56, 2.5, 2, 1, 'Apple', 'Mango']


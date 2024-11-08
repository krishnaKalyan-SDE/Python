#declaration pf tuple
tuple=(1,2,3,4)
print(tuple)  #(1, 2, 3, 4)

#another way to declare tuple
tuple1=1,2,3,4
print(tuple1)

for i in range(4):
    print(tuple[i],end=" ") #1 2 3 4

nums=(1)
print(type(nums)) #<class 'int'>...it is not utple now 

nums1=(1,)
print(type(nums1))  #<class 'tuple'>


#tuple unpacking
days=('Monday','Tuesday','Wednesday')
x,y,z=(days)
print(days) #('Monday', 'Tuesday', 'Wednesday')

#list inside tuple
tu=(1,2,3,['Monday','Tuesday','Wednesday'])
print(tu)

print(tu[3].pop())

tu[3].append("We made it ")
print(tu)

num=list((1,2,3))
print(num)  #[1, 2, 3]

x=str(('x','y','y'))
print(x)



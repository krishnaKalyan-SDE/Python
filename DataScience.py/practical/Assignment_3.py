x=int(input("Enter x: "))
y=int(input("Enter y: "))

#Arithmetic operator_
add=x+y
sub=x-y
mul=x*y
floor_div=x//y
div=x/y
mod=x%y
power=x**y

print("Arithmetic Operator(+,-,*,/,//,%,**): ")
print("add",add)
print("sub",sub)
print("mul",mul)
print("div",div)
print("floor_div",floor_div)
print("mod",mod)
print("power",power)
print(end='\n')

#Bitwise Operator
print("BitWise Operator(&,^,|):")
a=x&y
b=x^y
c=x|y
d=~x
e=x>>1
f=x<<1
print("use of & operator:",a)
print("use of | operator:",c)
print("use of ^ operator:",b)
print("use of left-shift:",f)
print("use of right-shift:",e)
print("use of not operator:",d)
print(end='\n')

#logical Operator
print("Logical Operator: ")
if x>1 and y<10:
    print("Successful use of and operator")
elif x<1 or y>10:
    print("successful use of or operator")
elif not(x<1 and y<10):
    print("successful use of not operator")
else:
    print("understood use of logical operator")
print(end="\n")

#comparison operator
print("Comparison operator: ")
if x==y:
    print("Seccessful use of == operator")
elif x!=y:
    print("Seccessful use of != operator")
elif x>y:
     print("Seccessful use of > operator")
elif x<y:
     print("Seccessful use of < operator")
elif x>=y:
    print("Seccessful use of >= operator")
elif x<=y:
    print("Seccessful use of <= operator")
else:
    print("successfully learnt comparison operator")
print(end="\n")

#identity Operator
num1=5
num2=5
print(num1 is num2)

list1=[1,2,3,4]
list2=[1,2,3,4]
print(list1 is not list2 )


#Membership operator
print("Membership Operator: ")
list=[1,2,3,4,5,6,7,8,9,10]
print(2 in list)

dict={1:"Ram",2:"Lakshman",3:"Hanuman"}
print(4 in dict)

tuple=(1,2,3,4,5)
print(2 not in tuple)


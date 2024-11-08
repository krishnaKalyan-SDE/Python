# x=3
# y=4
# print("AND Operation ",x&y)
# print("OR Operation ",x|y)
# print("XOR Operation ",x^y)
# print("NOT Operation ",~y)

# p=float(input("Enter principal amount: "))
# r=float(input("Enter rate:  "))
# t=float(input("Enter time: "))
# SI=(p*r*t)/100
# print(f"SI is {SI}")


#swap the value of two no
# a=10
# b=20
# print("Bfore swapping",a,b)
# temp=a
# a=b
# b=temp
# print("After swapping",a,b)

#leap year
# user_Input=int(input("Enter year: "))
# if (user_Input%4==0 and user_Input%100!=0) or (user_Input%400==0):
#     print(f"{user_Input} is a leap year")
# else:
#     print(f"{user_Input} is not a leap year")

# #factorial of a number
# n=int(input("Enter a number: "))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

# #check prime  no                           //Wrong(X)//
# n=int(input("Enter no: "))
# if n==1:
#     print(f"{n} is neither prime nor composite")
# if n==2:
#     print(f"{n} is only even prime")
# for i in range(2,n):
#     if (n%i==0 and n!=0):
#         print(f"{n} is not prime")
#         break
#     else:
#         print(f"{n} is prime")


#fibonacci sequence
n=int(input("Enter n: "))
a,b=0,1
count=0
while count<n:
    print(a,end=" ")
    a,b=b,a+b
    count+=1




# #Reverse a string
# s="Krishna"
# # print(s[-1::-1])
# print(s[::-1])

# #count vowels in string
# s=input("Enter string: ")
# count=0
# vowels="aeiouAEIOU"
# for char in s:
#     if char in vowels:
#         count+=1
# print(count)

# #SUM OF first n terms
# n=int(input("Enter nth term: "))
# sum=0
# for i in range(n+1):
#     sum=sum+i
# print(sum)

# #sum of natural no
# n=int(input("Enter nth term: "))
# sum=(n*(n+1))/2
# print(sum)

# #find largest of three no
# a=int(input("Enter a:"))
# b=int(input("Enter b:"))
# c=int(input("Enter c:"))
# if a>b and b>c:
#     print(f"{a} is largest")
# elif b>a and b>c:
#     print(f"{b} is largest")
# else:
#     print(f"{c} is largest")


# #simple calculator
# user=input("Enter (+,-,*,/,%):")
# first_no=float(input("Enter fitrst No: "))
# second_no=float(input("Enter second No: "))
# add=first_no+second_no
# sub=first_no-second_no
# mul=first_no*second_no
# div=first_no/second_no
# mod=first_no%second_no
# if user=='+':
#     print(f"Addition is {add}")
# elif user=='-':
#      print(f"Substraction is {sub}")
# elif user=='*':
#       print(f"Multiplication is {mul}")
# elif user=='/':
#      print(f"Division is {div} ")
# elif user=='%':
#      print(f"Modulus is {mod}")
# else:
#      print("Invalid Input")
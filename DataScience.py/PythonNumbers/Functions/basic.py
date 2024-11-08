# def fun(a,b):
#     return a+b

# add=fun(2,3)
# print(add)

# #even or odd
# def evenOdd(n):
#     if n%2==0:
#         return 'Even'
#     else:
#         return 'Odd'
    
# # EvenOdd=evenOdd(6)
# # print(EvenOdd)

# # print(evenOdd(7))
# # print(evenOdd(int(input())))
# user=int(input("Enter n to find even/odd: "))
# print(evenOdd(user))


# #factorial
# def factorial(n):
#     sum=1
#     for i in range(1,n+1):
#         sum=sum*i
#     return sum
# print(factorial(int(input("Enter n to calculate factorial: "))))

# def studentData(name,age='18',grade='A+'):
#     x=f"Name={name},age={age},grade={grade}"
#     return x
# name=input("Enter name: ")
# print(studentData(name))
        
# #prime
# def prime(n):
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             count=count+1
#     if count>2:
#         return ' Not prime'
#     else:
#         return 'prime'
    
# print(prime(int(input("Enter n to know prime or not:"))))

# #calculator
# def calculator(num1,num2,opr):
#     add=num1+num2
#     mul=num1*num2
#     div=num1/num2
#     sub=num1-num2
#     mod=num1%num2
#     if opr==1:
#         print("Addition is ",add)
#     elif opr==2:
#         print("Multiplication is ",mul)
#     elif opr==3:
#         if num2==0:
#             print("INvalid")
#         else:
#             print("Division is ",div)
#     elif opr==4:
#             print("subtraction is ",sub)
#     elif opr==5:
#         print("Modulus is ",mod)
#     else:
#         print("Invalid")

# print("Choose from below given operations: ")       
# print("Addition:",1)
# print("Multiplication:",2)
# print("Division:",3)
# print("Subtraction:",4)
# print("Modulus:",5)

# opr=int(input("Enter opr: "))

# num1=float(input("Enter num1: "))
# num2=float(input("Enter num2: "))
        
# calculator(num1,num2,opr)

def function(*args):
    for arg in args:
        print(arg)
print(function("Apple","mango","Tomato","PineApple","CustardApple"))

def func(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
dictionary={"first":"Apple","second":"Google","third":"Microsoft","fourth":"Firebase"}
print(func(**dictionary))


def fun(n):
    """even or odd"""
    """x"""
    if n%2==0:
      print("even")
    else:
      print("odd")
    
print(fun.__doc__)

def fibonacii(n):
   p,q=0,1
   r=p+q
   print(p,q,end=" ")
   for i in range(n):
      r=p+q
      print(r,end=" ")
      p=q
      q=r
      
fibonacii(int(input("Enter no to find fibonacci till that no: ")))


      




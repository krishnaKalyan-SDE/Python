user=input("Enter Operation to be performed: ")
a=3
b=10
if user=='+':
    print(f"Addition is {a+b}")
elif user=='-':
     print(f"Substraction is {a-b}")
elif user=='*':
     print(f"Multiplication is {a*b}")
elif user=='/':
     print(f"Division is {a/b} ")
else:
     print(f"Invalid input {user } ")
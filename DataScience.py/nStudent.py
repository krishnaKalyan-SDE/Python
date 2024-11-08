import pandas as pd
name=[]
email=[]
branch=[]

n=int(input("Enter n: "))

for i in range(n):
    print(f"Record of student {i+1}: ")
    name1=input("Enter name : ")
    email1=input("Enter email : ")
    branch1=input("Enter branch : ")
     
    name.append(name1)
    email.append(email1)
    branch.append(branch1)

df=pd.DataFrame({
    "Name":name,
    "Email":email,
    "Branch":branch
})

df.to_excel("Record.xlsx")
print("Record successful")


    

     
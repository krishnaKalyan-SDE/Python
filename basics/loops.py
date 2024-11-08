"""for i in range(4):
    print(f"Student {i+1} : ")
    phy=int(input("Enter Physics marks "))
    chem=int(input("Enter Chemistry marks "))
    math=int(input("Enter Maths marks "))
    total=phy+chem+math
    print("Total Marks of student ",i+1,"is ",total)
    print("\n")"""
  
    

#output
"""Enter Physics marks 100
Enter Chemistry marks 99
Enter Maths marks 98
Total Marks of student  1 is  297


Enter Physics marks 97
Enter Chemistry marks 96
Enter Maths marks 95
Total Marks of student  2 is  288


Enter Physics marks 94
Enter Chemistry marks 93
Enter Maths marks 92
Total Marks of student  3 is  279


Enter Physics marks 100
Enter Chemistry marks 99
Enter Maths marks 88
Total Marks of student  4 is  287"""

physics=[]
chemistry=[]
math=[]

for i in range(3):
    physics.append(int(input("Enter physics marks ")))
    chemistry.append(int(input("Enter chemistry marks ")))
    math.append(int(input("Enter math marks ")))

    x.append(physics[i]+chemistry[i]+math[i])
    print(f"total marks of student{i}",x)




    

# name,age=input("Enter name and age :").split(",")
# if (name[0]=='a' or 'A') and int(age)>14:
#     print("You can chant Hare Krishna mahamantra")
# else:
#     print("You must chant mahamantra!!!")


age=int(input("Enter your age:"))
if age>=0 and age<7:
    print("Ticket is free!!!")
elif age>=7 and age<25:
    print("Ticket is 150")
elif age>=25 and age<50:
    print("Ticket is 200 ")
else:
    print("Ticket is 230" )
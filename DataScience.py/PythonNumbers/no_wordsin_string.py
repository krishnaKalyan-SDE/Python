# user=input("Enter string: ").strip(" ")
# count=1
# for i in range(len(user)):
#     if user[i]==" ":
#         count+=1        
# print(count)

"""
no_of_students=int(input("Enter no of students: "))
for i in range(no_of_students):
    marks=int(input(f"Enter marks of student {i+1}: "))
    if marks>=19 and marks<=20:
        print("A+")
    elif marks>=17 and marks<=18:
        print("A")
    elif marks>=15 and marks<=16:
        print('B+')
    elif marks>=13 and marks<=16:
        print("B")
    elif marks>=11 and marks<=12:
        print("C")
    elif marks>=8 and marks<=10:
        print("D")
    elif marks>=0 and marks<=7:
        print("F")
    else:
        print("Marks out of range")
"""

weakly_attendance=[]#no of lectures attended on each day
attendence=[]
for i in range(6):
    lectures_attended_day=int(input(f"Enter lectures attended in {i+1} day: "))
    weakly_attendance.append(lectures_attended_day)
    percent_attendence=((lectures_attended_day)/6)*100
    attendence.append(percent_attendence)
# print(weakly_attendance)
# print(attendence)
# for i in range(len(attendence)):
#         if attendence[i]<75:
# print(i+1,end=",")




weakly_attendance=[]#no of lectures attended on each day
attendence=[]
for i in range(6):
    lectures_attended_day=int(input(f"Enter lectures attended in {i+1} day: "))
    weakly_attendance.append(lectures_attended_day)
    percent_attendence=((lectures_attended_day)/6)*100
    attendence.append(percent_attendence)
print(weakly_attendance)
print(attendence)
for i in range(len(attendence)):
        if attendence[i]<75:
         print(i+1,sep=",",end=" ")



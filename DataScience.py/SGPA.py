import pandas as pd

#credit for each subject is given below
subject=['Maths','DM','DE','python','OE','Phy','chem','FP','practical']
credit=[3,3,2,3,0,1,1,1,2]
score_list=[]
grade_point=[]



for i in range(len(credit)):
    marks=int(input(f'Enter marks of sub {i+1}: '))
    if marks>=90:
     GradePoint=10
    elif marks>=80 and  marks<90:
     GradePoint=9 
    elif marks>=70 and marks<80:
      GradePoint=8
    elif marks>=60 and marks<70:
      GradePoint=7
    elif marks>=50 and marks<60:
      GradePoint=6
    elif marks>=40 and marks<50:
      GradePoint=5

    grade_point.append(GradePoint)

    score=credit[i]*GradePoint
    score_list.append(score)
print(score_list)
    

sum=0
for i in range(len(score_list)):
  sum=(score_list[i]+sum)
print(f"Total score is {sum}")

total=0
for i in range(len(credit)):
 total=(credit[i]+total)
print(f"Total score is {total}")

GPA=sum/total
print(GPA)

df=pd.DataFrame({
  "Subject":subject,
  "Credit":credit,
  "GradePoint":grade_point,
   "Score":score_list

})

df.to_excel("GPA Calculation in GPA.xlsx",index=False)
print("GPA calulation successfull")

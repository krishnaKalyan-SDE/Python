import pandas as pd

#Input for first student
name1 = input("Enter the first student's name: ")
email1 = input("Enter the first student's email: ")
branch1 = input("Enter the first student's branch: ")

#Determine the MDM value based on the branch for the first student
if branch1 == "IT":
    mdm1 = "Data Science"
elif branch1 == "Mech":
    mdm1 = "CAD"
else:
    mdm1 = "OTHER"

#nput for second student
name2 = input("Enter the second student's name: ")
email2 = input("Enter the second student's email: ")
branch2 = input("Enter the second student's branch: ")

#Determine the MDM value based on the branch for the second student
if branch2 == "IT":
    mdm2 = "Data Science"
elif branch2 == "Mech":
    mdm2 = "CAD"
else:
    mdm2 = "OTHER"

#Create a DataFrame with the input data for both students
df = pd.DataFrame({
    "Name": [name1, name2],
    "Email": [email1, email2],
    "Branch": [branch1, branch2],
    "MDM": [mdm1, mdm2]
})

#Write the DataFrame to an Excel file
df.to_excel("student_records.xlsx", index=False)

print("Data has been written to student_records.xlsx")
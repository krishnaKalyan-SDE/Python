


import pandas as pd

# Initialize lists to store the data for each student
physics_marks = []
chemistry_marks = []
math_marks = []
grades = []

# Input marks for each student
for i in range(1):
    print(f"Enter marks for student {i+1}:")
    physics = int(input(f"Enter Physics Marks: "))
    chemistry = int(input(f"Enter Chemistry Marks: "))
    math = int(input(f"Enter Math Marks: "))
    
    # Calculate sum and percentage
total_marks = physics + chemistry + math
percent = (total_marks / 300) * 100
    
    # Store the data in the lists
physics_marks.append(physics)
chemistry_marks.append(chemistry)
math_marks.append(math)
grades.append(percent)

# Create a DataFrame using the collected data
df = pd.DataFrame({
    "Physics": physics_marks,
    "Chemistry": chemistry_marks,
    "Maths": math_marks,
    "Grade (%)": grades
})

# Save the DataFrame to an Excel file
df.to_excel("Marksheet.xlsx", index=False)

print("Data has been written to Marksheet.xlsx")

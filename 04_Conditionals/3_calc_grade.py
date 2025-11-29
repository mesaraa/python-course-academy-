# Input marks from 0 to 100
marks = float(input("Enter marks (0-100): "))

# Use conditions to assign grade
if marks >= 90 and marks <= 100:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
elif marks >= 0:
    grade = "F"
else:
    grade = "Invalid marks"

# Print the grade
print("Grade:", grade)

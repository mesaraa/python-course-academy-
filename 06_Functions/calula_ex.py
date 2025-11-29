def calculate_total(m1, m2, m3):
    return m1 + m2 + m3

def calculate_average(total):
    return total / 3

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))

total = calculate_total(m1, m2, m3)
avg = calculate_average(total)
grade = calculate_grade(avg)

print("\n--- Result ---")
print("Total Marks:", total)
print("Average Marks:", avg)
print("Grade:", grade)

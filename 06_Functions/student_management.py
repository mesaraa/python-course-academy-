
"""
Create a function-based program that manages students in a school.
The system must support:

1. Add student (name, roll, class)
2. View all students
3. Search student by roll number
4. Remove student
5. Exit

Use list of dictionaries and divide work into reusable functions.
"""

def menu():
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Exit")    

def add_student(students):
    name = input("Enter student name: ")
    roll = input("Enter roll number of student: ")
    grade = input("Enter class of student: ")

    student = {
        "name": name,
        "roll": roll,
        "grade": grade
    }
    students.append(student)
    print("Student added!\n")

def view_students(students):
    if not students:
        print("No students found.\n")
        return

    print("\n--- Student List ---")
    for s in students:
        print(f"{s['roll']} - {s['name']} ({s['grade']})")
    print()

def search_student(students):
    roll = input("Enter roll to search: ")

    for s in students:
        if s['roll'] == roll:
            print("Student Found:", s)
            print()
            return
    print("Student not found.\n")

def remove_student(students):
    roll = input("Enter roll to remove: ")

    for s in students:
        if s['roll'] == roll:
            students.remove(s)
            print("Student removed!\n")
            return
    print("Student not found.\n")

students = []


while True:
    menu()
    ch = input("Choose option: ")

    if ch == "1":
        add_student(students)
    elif ch == "2":
        view_students(students)
    elif ch == "3":
        search_student(students)
    elif ch == "4":
        remove_student(students)
    elif ch == "5":
        break
    else:
        print("Invalid option\n")
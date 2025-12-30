class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display_details(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)

# Creating object
s1 = Student("Amit", 101)

# Calling method
s1.display_details()

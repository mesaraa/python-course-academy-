# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, My name is {self.name}.")

# Child class (inherits Person)
class Student(Person):
    def __init__(self, name, age, roll_number):
        # calling parent constructor
        super().__init__(name, age)
        self.roll_number = roll_number
    
    def student_info(self):
        print("Student Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Roll Number: {self.roll_number}")

# creating object
s1 = Student("Sara", 15, 768)

# calling methods
s1.greet()
s1.student_info()

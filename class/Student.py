#Default constructor
class Student:
    def get(self):
        self.name = input("Enter Name: ")
        self.roll_no = input("Enter Roll Number: ")

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)

s1 = Student()
s1.get()
s1.display()

#Parameterised constructor
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)

s1 = Student("Prajakta", 14)
s1.display()


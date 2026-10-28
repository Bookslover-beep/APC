class Student:
    def get(self):
        self.name = input("Enter Name: ")
        self.roll_no = input("Enter Roll Number: ")

    def display(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)

s1 = Student()
s1.get()
s1.display()

class Addition:
first = 0
second = 0
answer = 0

def _init_(self,f,s):
    self.first = f
    self.second = s

    def display(self):
        print("First number = ",+str(self.first))
        print("Second number = ",+str(self.second))
        print("Addition of two number = ",+str(self.answer))
    def calculate(self):
        self.answer = self.first + self.second
obj = Addition(1000, 2000)
obj.calculate()
obj.display()
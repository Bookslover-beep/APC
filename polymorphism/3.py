# Polymorphism through operator overloading

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __str__(self):
        return str(self.value)


print("\nOperator overloading")
first_number = Number(10)
second_number = Number(20)
print("Sum:", first_number + second_number)
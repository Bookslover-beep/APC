#32.Create separate functions for addition, subtraction, multiplication, and division. Pass these functions as arguments to another function called calculate().

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): 
    return a / b if b != 0 else "Error: Division by zero"

def calculate(func, a, b):
    return func(a, b)

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\n--- Calculation Results ---")
print(f"Addition ({a} + {b}) = {calculate(add, a, b)}")
print(f"Subtraction ({a} - {b}) = {calculate(sub, a, b)}")
print(f"Multiplication ({a} * {b}) = {calculate(mul, a, b)}")
print(f"Division ({a} / {b}) = {calculate(div, a, b)}")
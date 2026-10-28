#1.Create a Python module calculator.py containing functions for addition, subtraction, multiplication, and division. 
#Create another program that imports the module and performs calculations based on user input. 


import calculator

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print(calculator.add(x, y))
elif op == '-':
    print(calculator.subtract(x, y))
elif op == '*':
    print(calculator.multiply(x, y))
elif op == '/':
    print(calculator.divide(x, y))
else:
    print("Invalid operator")
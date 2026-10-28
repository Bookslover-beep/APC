#36.Use a lambda function to find the maximum of two numbers.

max_two = lambda a, b: a if a > b else b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"The maximum of {a} and {b} is {max_two(a, b)}")
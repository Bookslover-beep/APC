#3.Define a function that accepts two numbers and returns the greater number.

def greater(a, b):
    if a > b:
        return a
    else:
        return b

a = int(input("Enter any number:"))
b = int(input("Enter any number:"))

print(f"Greater is {greater(a, b)}")
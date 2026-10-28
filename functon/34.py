#34.Create a lambda function that returns the cube of a number.

cube = lambda x: x ** 3

num = int(input("Enter a number: "))
print(f"Cube of {num} = {cube(num)}")
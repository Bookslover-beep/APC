#33.Write a lambda function to calculate the square of a given number.

square = lambda x: x ** 2

num = int(input("Enter a number: "))
print(f"Square of {num} = {square(num)}")
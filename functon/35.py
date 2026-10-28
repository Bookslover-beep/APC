#35.Write a lambda function that returns True if a number is even and False otherwise.

is_even = lambda x: x % 2 == 0

num = int(input("Enter an integer: "))
print(f"Is {num} even? {is_even(num)}")
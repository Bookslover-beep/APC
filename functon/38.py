#38.Take a list of numbers, use map() and a lambda function to generate a list containing their squares.

squares_func = lambda lst: list(map(lambda x: x ** 2, lst))

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Squares =", squares_func(numbers))
#39.Use map() with lambda to calculate the cube of every element in a list.

cubes_func = lambda lst: list(map(lambda x: x ** 3, lst))

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Cubes =", cubes_func(numbers))
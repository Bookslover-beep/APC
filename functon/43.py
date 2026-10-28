#43.Use filter() and lambda to extract positive numbers from a list.

get_positives = lambda lst: list(filter(lambda x: x > 0, lst))

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Positive numbers =", get_positives(numbers))
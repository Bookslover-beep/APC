#44.Take a list of numbers, use filter() and lambda to find numbers greater than 50.

filter_gt_50 = lambda lst: list(filter(lambda x: x > 50, lst))

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Numbers greater than 50 =", filter_gt_50(numbers))
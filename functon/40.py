#40.Take two lists of numbers, use map() and lambda to create a third list containing the sum of corresponding elements.

sum_two_lists = lambda lst1, lst2: list(map(lambda x, y: x + y, lst1, lst2))

list1 = list(map(int, input("Enter first list of numbers separated by spaces: ").split()))
list2 = list(map(int, input("Enter second list of numbers separated by spaces: ").split()))

print("Corresponding Sums =", sum_two_lists(list1, list2))
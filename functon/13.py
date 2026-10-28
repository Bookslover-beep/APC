#13.Write a function that accepts a list of numbers and returns their average.

def list_average(lst):
    return sum(lst) / len(lst) if lst else 0

numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
print("Average =", list_average(numbers))
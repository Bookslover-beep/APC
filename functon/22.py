#22.Write a function that accepts a list of numbers and returns the minimum, maximum, sum, and average.

def list_statistics(lst):
    if not lst:
        return None, None, 0, 0
    return min(lst), max(lst), sum(lst), sum(lst) / len(lst)

numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
mn, mx, sm, avg = list_statistics(numbers)

if numbers:
    print(f"Minimum = {mn}")
    print(f"Maximum = {mx}")
    print(f"Sum = {sm}")
    print(f"Average = {avg}")
else:
    print("The list is empty.")
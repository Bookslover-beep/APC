#16.Create a function to find the second-largest number in a list.

def second_largest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[-2] if len(unique) >= 2 else None

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

result = second_largest(numbers)
if result is not None:
    print(f"The second-largest number is: {result}")
else:
    print("List must contain at least two unique elements.")
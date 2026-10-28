#29.Write a recursive function to search for an element in a sorted list using binary search.

def binary_search(lst, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if lst[mid] == x:
            return mid
        elif lst[mid] > x:
            return binary_search(lst, low, mid - 1, x)
        else:
            return binary_search(lst, mid + 1, high, x)
    return -1

lst = list(map(int, input("Enter sorted numbers separated by spaces: ").split()))
x = int(input("Enter element to search for: "))

result = binary_search(lst, 0, len(lst) - 1, x)
if result != -1:
    print(f"Element found at index {result}.")
else:
    print("Element not found in the list.")
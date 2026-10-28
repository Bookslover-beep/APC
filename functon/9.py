#9.Write a function that accepts a list of numbers and returns the largest element without using the built-in max() function.

def largest_element(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

if numbers:
    print("The largest element is:", largest_element(numbers))
else:
    print("The list is empty.")
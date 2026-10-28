#14.Define a function that accepts a list and an element and returns the number of times that element occurs.

def element_frequency(lst, elem):
    return lst.count(elem)

elements = input("Enter elements separated by spaces: ").split()
target = input("Enter element to find frequency for: ")
print(f"Frequency of '{target}' =", element_frequency(elements, target))
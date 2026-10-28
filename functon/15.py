#15.Write a function that accepts a list and returns a new list containing only unique elements

def unique_elements(lst):
    return list(set(lst))

elements = input("Enter elements separated by spaces: ").split()
print("Unique elements =", unique_elements(elements))
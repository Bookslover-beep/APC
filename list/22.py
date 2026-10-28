#22.Find common elements between two lists.
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
print("list1 =",list1)
print("list2 =",list2)
print()

common_elements = list(set(list1) & set(list2))
print("common_elements =",common_elements)
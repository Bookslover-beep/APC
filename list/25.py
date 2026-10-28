#25.Remove all duplicate elements while preserving the original order.
numbers = [1, 2, 2, 3, 4, 3, 5, 1]
print("numbers =",numbers)
print()
unique_order = []
for num in numbers:
    if num not in unique_order:
        unique_order.append(num)

print("unique_order =",unique_order)

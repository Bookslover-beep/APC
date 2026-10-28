#23.Count the frequency of each element in a list.
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print("numbers =",numbers)
frequency = {}

for item in numbers:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print("frequency =",frequency)
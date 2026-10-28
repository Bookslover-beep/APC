#15.Find the second largest element in a list.
num = [45, 12, 89, 3, 67, 24]
print("num =",num)
n = list(sorted(set(num)))
print("Sorted List =",n)
print("Second largest element:", n[-2])
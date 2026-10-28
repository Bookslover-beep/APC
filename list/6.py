#6.Write a program to find the largest and smallest number in a list without using max() or min().
num = [15, 10, 40, 14, 50]
print("num = ",num)
largest = num[0]
smallest = num[0]
for n in num:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n
print("Largest number:", largest)
print("Smallest number:", smallest)
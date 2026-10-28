#Write a PYTHON program to print sum of even numbers up to n

n = int(input("Enter the number: "))

i = 1
total = 0

while i <= n:
    if i % 2 == 0:
        total += i
    i += 1

print("Sum of even numbers is", total)
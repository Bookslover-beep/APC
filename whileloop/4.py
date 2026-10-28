#Write a PYTHON program to print sum of natural numbers up to n

n = int(input("Enter the number:"))
i=1
total = 0
while i <= n:
    total+=i
    i+=1

print(f"Sum of all number is {total}")
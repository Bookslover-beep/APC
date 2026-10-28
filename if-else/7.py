#Write a PYTHON program to find smallest of three numbers

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if a <= b and a <= c:
    print(f"The smallest number is {a}")
elif b <= a and b <= c:
    print(f"The smallest number is {b}")
else:
    print(f"The smallest number is {c}")
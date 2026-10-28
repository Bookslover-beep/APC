#Write a python program to check the entered number is prime or not using while loop in python 
num = int(input("Enter a number: "))

i = 2
is_prime = True

if num <= 1:
    is_prime = False

while i < num:
    if num % i == 0:
        is_prime = False
        break
    i += 1

if is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
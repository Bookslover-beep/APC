#Python program to check whether the square root of number is prime or not
import math

num = int(input("Enter a number: "))
root = int(math.sqrt(num))

if root * root == num:
    is_prime = True

    if root < 2:
        is_prime = False
    else:
        for i in range(2, root):
            if root % i == 0:
                is_prime = False
                break

    if is_prime:
        print(root, "is prime")
    else:
        print(root, "is not prime")
else:
    print("Square root is not an integer")
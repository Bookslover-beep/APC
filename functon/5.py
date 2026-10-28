#5.Write a function is_prime(n) that returns True if a number is prime; otherwise, returns False.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter any number: "))
print(is_prime(n))
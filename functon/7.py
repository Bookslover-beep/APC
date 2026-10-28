#7.Write a function that accepts n and returns the sum of the first n natural numbers
def sum_natural(n):
    return n * (n + 1) // 2

n = int(input("Enter a positive integer: "))
print(f"Sum of the first {n} natural numbers =", sum_natural(n))
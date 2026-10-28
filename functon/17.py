#17.Write a function that accepts n and returns the first n Fibonacci numbers.

def fibonacci_series(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

n = int(input("Enter the number of terms: "))
print(f"First {n} Fibonacci numbers:", fibonacci_series(n))
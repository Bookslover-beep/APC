#42.Take a list of integers, use filter() with an appropriate lambda expression to identify prime numbers.

is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
get_primes = lambda lst: list(filter(is_prime, lst))

numbers = list(map(int, input("Enter integers separated by spaces to find primes: ").split()))
print("Prime numbers =", get_primes(numbers))
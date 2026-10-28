#41.Take a list of integers, use filter() and lambda to extract all even numbers.

filter_evens = lambda lst: list(filter(lambda x: x % 2 == 0, lst))

numbers = list(map(int, input("Enter integers separated by spaces: ").split()))
print("Even numbers =", filter_evens(numbers))
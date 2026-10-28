#30.Convert a decimal number into binary using recursion without using Python's built-in conversion functions.

def decimal_to_binary(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    return decimal_to_binary(n // 2) + str(n % 2)

n = int(input("Enter a decimal number: "))
if n < 0:
    print("Please enter a non-negative integer.")
else:
    print(f"Binary representation = {decimal_to_binary(n)}")
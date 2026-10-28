#8.Create a function power(base, exponent) to calculate the value of base raised to exponent.

def power(base, exponent):
    return base ** exponent

b = float(input("Enter the base: "))
e = int(input("Enter the exponent: "))
print(f"{b} raised to the power of {e} =", power(b, e))

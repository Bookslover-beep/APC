#37.Create a lambda function to calculate simple interest using principal, rate, and time.

si = lambda p, r, t: (p * r * t) / 100

p = float(input("Enter principal amount: "))
r = float(input("Enter annual interest rate (%): "))
t = float(input("Enter time (in years): "))

print(f"Simple Interest = {si(p, r, t):.2f}")
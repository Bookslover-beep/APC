#4.Create a function simple_interest(p, r, t) to calculate simple interest.

def simple_interest(p, r, t):
    return (p * r * t) / 100

p = float(input("Enter Principal amount: "))
r = float(input("Enter Annual Rate of Interest: "))
t = float(input("Enter Time (in years): "))

print(f"Simple Interest = {simple_interest(p, r, t)}")
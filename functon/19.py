#19.Write a function that accepts the number of units consumed and calculates the electricity bill according to predefined slabs.

def calculate_electricity_bill(units):
    if units <= 100:
        bill = units * 1.5
    elif units <= 300:
        bill = 100 * 1.5 + (units - 100) * 3.0
    else:
        bill = 100 * 1.5 + 200 * 3.0 + (units - 300) * 5.0
    return bill

units = int(input("Enter electricity units consumed: "))
print(f"Total Electricity Bill = {calculate_electricity_bill(units)}")
#26.Develop a modular program using functions to calculate electricity bills using different consumption slabs. Include fixed charges, taxes, and discounts.

def calculate_electricity_bill(units, fixed_charge=50.0, tax_pct=5.0, discount_pct=0.0):
    if units <= 100:
        energy_charge = units * 1.5
    elif units <= 300:
        energy_charge = 100 * 1.5 + (units - 100) * 3.0
    else:
        energy_charge = 100 * 1.5 + 200 * 3.0 + (units - 300) * 5.0
    
    subtotal = energy_charge + fixed_charge
    tax = subtotal * (tax_pct / 100)
    total_before_discount = subtotal + tax
    discount = total_before_discount * (discount_pct / 100)
    final_bill = total_before_discount - discount
    return final_bill

units = int(input("Enter units consumed: "))
fixed = float(input("Enter fixed charges: "))
tax = float(input("Enter tax percentage: "))
disc = float(input("Enter discount percentage: "))

print(f"Final Electricity Bill = {calculate_electricity_bill(units, fixed, tax, disc):.2f}")
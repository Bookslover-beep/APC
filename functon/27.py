#27.Create functions to calculate consultation charges, laboratory charges, medicine charges, room charges, and final bill. Apply discounts based on patient category.

def calculate_hospital_bill(consultation, lab, medicine, room, category):
    subtotal = consultation + lab + medicine + room
    
    category = category.lower()
    if category == "senior":
        discount_pct = 15.0
    elif category == "general":
        discount_pct = 5.0
    else:
        discount_pct = 0.0
        
    discount = subtotal * (discount_pct / 100)
    final_bill = subtotal - discount
    return subtotal, discount, final_bill

consultation = float(input("Enter consultation charges: "))
lab = float(input("Enter laboratory charges: "))
medicine = float(input("Enter medicine charges: "))
room = float(input("Enter room charges: "))
category = input("Enter patient category (Senior / General / Standard): ")

sub, disc_amt, final = calculate_hospital_bill(consultation, lab, medicine, room, category)
print(f"\nSubtotal = {sub:.2f}")
print(f"Discount Applied = {disc_amt:.2f}")
print(f"Final Hospital Bill = {final:.2f}")
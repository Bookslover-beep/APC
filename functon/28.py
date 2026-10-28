#28.Implement functions to add/remove products, calculate subtotal, apply coupon discounts, calculate GST, and generate the final invoice.

def subtotal_func(prices, quantities):
    return sum(p * q for p, q in zip(prices, quantities))

def apply_coupon(sub, coupon):
    return sub * 0.9 if coupon == "SAVE10" else sub

def calculate_gst(sub):
    return sub * 0.18

def generate_invoice(prices, quantities, coupon):
    sub = subtotal_func(prices, quantities)
    discounted = apply_coupon(sub, coupon)
    gst = calculate_gst(discounted)
    return sub, discounted, gst, discounted + gst

prices = list(map(float, input("Enter product prices separated by spaces: ").split()))
quantities = list(map(int, input("Enter product quantities separated by spaces: ").split()))
coupon = input("Enter coupon code (e.g., SAVE10 or press Enter for none): ").strip()

if len(prices) == len(quantities) and prices:
    sub, disc, gst, final = generate_invoice(prices, quantities, coupon)
    print("\n--- Invoice Summary ---")
    print(f"Subtotal = {sub:.2f}")
    print(f"After Discount = {disc:.2f}")
    print(f"GST (18%) = {gst:.2f}")
    print(f"Final Invoice Total = {final:.2f}")
else:
    print("Error: Prices and quantities lists must match in length and not be empty.")
#21.Create a function that accepts item prices and quantities and returns the total bill after applying a discount.

def total_bill(prices, quantities, discount_pct):
    subtotal = sum(p * q for p, q in zip(prices, quantities))
    discount = subtotal * (discount_pct / 100)
    return subtotal - discount

prices = list(map(float, input("Enter item prices separated by spaces: ").split()))
quantities = list(map(int, input("Enter item quantities separated by spaces: ").split()))
discount_pct = float(input("Enter discount percentage: "))

print(f"Final Total Bill = {total_bill(prices, quantities, discount_pct):.2f}")
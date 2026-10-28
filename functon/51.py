#51.Take a list of products with names, prices, and quantities, use functions and lambda expressions to:
#a)Calculate total value of each product. 
#b)Filter products costing more than ₹1,000. 
#c)Sort products according to total value.

calc_totals = lambda prods: list(map(lambda p: (p[0], p[1] * p[2]), prods))
filter_expensive = lambda prods: list(filter(lambda p: p[1] > 1000, prods))
sort_by_total = lambda prods: sorted(prods, key=lambda p: p[1] * p[2], reverse=True)

n = int(input("Enter number of products: "))
products = []

for _ in range(n):
    name = input("Enter product name: ")
    price = float(input("Enter unit price: "))
    qty = int(input("Enter quantity: "))
    products.append((name, price, qty))

if products:
    print("\n--- Product Processing Results ---")
    print("Total value of each product:", calc_totals(products))
    print("Products costing > 1,000 (unit price):", filter_expensive(products))
    print("Products sorted by total value:", sort_by_total(products))
else:
    print("No product records provided.")
#18.Create a shopping cart using a list.Perform:
#a.Add item b.Remove item c.Search item d.Display cart e.Count total items

shopping_cart = []

shopping_cart.append("Apple")
shopping_cart.append("Milk")
shopping_cart.append("Bread")
print("shopping_cart =",shopping_cart)
print()
shopping_cart.remove("Milk")
print("Removing item:\nshopping_cart =",shopping_cart)
print()
search_item = "Apple"
if search_item in shopping_cart:
    print(f"{search_item} is in the cart.")
else:
    print(f"{search_item} is not in the cart.")

print("Cart contents:", shopping_cart)
print("Total items:", len(shopping_cart))
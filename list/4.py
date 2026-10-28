#4. Create a list of numbers. Add:
#a.One element at the end
#b.One element at the beginning
#c.One element at a specified position
#Display the updated list

num = [10, 20, 30, 40, 50]
print("Original List:",num)
num.append(60)
num.insert(0, 5)
num.insert(3,25)
print("Updated List:",num)
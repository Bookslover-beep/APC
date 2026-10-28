#27. Store salaries of employees and determine:
#a.Highest salary b.Lowest salary c.Average salary d.Employees earning above ₹ 50,000
#e.Employees earning below ₹ 30,000
salaries = [45000, 60000, 25000, 80000, 28000, 52000, 35000, 90000, 22000, 55000]
print("salaries =",salaries)

highest = max(salaries)
lowest = min(salaries)
avg = sum(salaries) / len(salaries)

above_50k = [s for s in salaries if s > 50000]
below_30k = [s for s in salaries if s < 30000]

print("Highest salary:", highest)
print("Lowest salary:", lowest)
print("Average salary:", avg)
print("Employees earning above 50,000:", above_50k)
print("Employees earning below 30,000:", below_30k)
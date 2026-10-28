filter_rich = lambda emps: list(filter(lambda e: e[2] > 50000, emps))
give_raise = lambda emps: list(map(lambda e: (e[0], e[1], e[2] * 1.1), emps))
sort_by_salary = lambda emps: sorted(emps, key=lambda e: e[2])

#50.Take employee records containing name, department, and salary, use filter(), map(), and sorted() with lambda functions to:
#a)Find employees earning more than ₹50,000. 
#b)Increase salaries by 10%. 
#c)Sort employees according to salary.

n = int(input("Enter number of employees: "))
emps = []

for _ in range(n):
    name = input("Enter employee name: ")
    dept = input("Enter department: ")
    salary = float(input("Enter salary: "))
    emps.append((name, dept, salary))

if emps:
    print("\n--- Employee Processing Results ---")
    print("Employees earning > 50,000:", filter_rich(emps))
    print("Salaries after 10% hike:", give_raise(emps))
    print("Employees sorted by salary:", sort_by_salary(emps))
else:
    print("No employee records provided.")
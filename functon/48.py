#48.Take employee records containing name and salary, sort them according to salary using lambda.

sort_employees = lambda emps: sorted(emps, key=lambda x: x[1])

n = int(input("Enter number of employees: "))
emp_list = []
for _ in range(n):
    name = input("Enter employee name: ")
    salary = float(input("Enter salary: "))
    emp_list.append((name, salary))

print("Employees sorted by salary:", sort_employees(emp_list))
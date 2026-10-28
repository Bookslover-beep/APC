#20.Write a function that accepts basic salary and calculates gross salary after adding HRA and DA.

def gross_salary(basic):
    hra = basic * 0.4
    da = basic * 0.2
    return basic + hra + da

basic = float(input("Enter basic salary: "))
print(f"Gross Salary = {gross_salary(basic):.2f}")
#5.Create a module containing functions to calculate gross salary, deductions, and net salary for an employee. 

import salary_utils

basic_pay = 50000
print("Gross Salary:", salary_utils.calculate_gross(basic_pay))
print("Deductions:", salary_utils.calculate_deductions(basic_pay))
print("Net Salary:", salary_utils.calculate_net(basic_pay))
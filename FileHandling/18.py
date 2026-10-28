#18. Store employee ID, name, department, and salary in a file. Write functions to:  
#•Display all employees.  
#•Find the highest-paid employee.  
#•Calculate average salary.  
#•Display employees earning above a given salary. 


with open("emp.txt", "w") as f:
    f.write("101, Neha, HR, 50000\n")
    f.write("102, Prajakta, IT, 75000\n")
    f.write("103, Riya, Finance, 60000\n")

def display_all():
    with open("emp.txt", "r") as f:
        print(f.read())

def highest_paid():
    with open("emp.txt", "r") as f:
        highest = 0
        emp_name = ""
        for line in f:
            parts = [p.strip() for p in line.split(",")]
            sal = float(parts[3])
            if sal > highest:
                highest = sal
                emp_name = parts[1]
        print("Highest paid:", emp_name, highest)

def avg_salary():
    with open("emp.txt", "r") as f:
        total = 0
        count = 0
        for line in f:
            parts = [p.strip() for p in line.split(",")]
            total += float(parts[3])
            count += 1
        print("Average salary:", total / count)

def above_salary(threshold):
    with open("emp.txt", "r") as f:
        for line in f:
            parts = [p.strip() for p in line.split(",")]
            if float(parts[3]) > threshold:
                print(parts[1], parts[3])

display_all()
highest_paid()
avg_salary()
above_salary(55000)
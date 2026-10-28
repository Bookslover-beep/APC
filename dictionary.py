#Dictionary
#creating dictionary
emp={"Name": "Prajakta", "Age" : 20, "Salary" : 30000, "Company" : "TCS"}
print(type(emp))
print("Printing employee details...")
print(emp)
print()

#using dict()
emp=dict({"Name": "Prajakta", "Age" : 20, "Salary" : 26000, "Company" : "TCS"})
print(type(emp))
print("Printing employee details...")
print(emp)
print()

#accessing dictionary values
emp={"Name": "Sakshi", "Age" : 20, "Salary" : 26000, "Company" : "TCS"}
print(type(emp))
print("Printing employee details...")
print("Name: ", emp["Name"])
print("Age: ", emp["Age"])
print("Salary: ", emp["Salary"])
print("Company: ", emp["Company"])
print()

#dictionary methods
emp = {"Name": "Sakshi", "Age": 20, "Salary": 26000, "Company": "TCS"}

print(emp.get("Name"))  
print(emp.keys())
print(emp.values())
print(emp.items())

emp.update({"Salary": 30000, "Designation": "Developer"})
print(emp)

print(emp.pop("Company"))
print(emp)

print(emp.popitem())
print(emp)

emp.setdefault("City", "Mumbai")
print(emp)

new_emp = emp.copy()
print(new_emp)

emp.clear()
print(emp)

keys = ["Name", "Age", "Salary"]
default_dict = dict.fromkeys(keys, None)
print(default_dict)


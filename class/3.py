#Write python program to demonstrate multilevel inheritance. You need to define three classes: 
#1.Person: This class will represent a person with basic attributes like name and age. 
#2.Employee: This class will inherit from Person and add additional attributes related to an employee, such as employee ID and salary. 
#3.Manager: This class will inherit from Employee and add additional functionality related to a manager, such as department and team size. 
#Class Details: 
#1.Person class should have the following attributes: 
#name: The name of the person.age: The age of the person. 
#Method: 
#display_person_info(): Displays the persons name and age. 
#2.Employee class should inherit from Person and add the following attributes: 
#employee_id: The unique employee ID. 
#salary: The salary of the employee. 
#Method: 
#display_employee_info(): Displays the employees ID and salary, as well as the name and age using the Person class& s method. 
 
#3. Manager class should inherit from Employee and add the following attributes: 
#department: The department managed by the manager. 
#team_size: The size of the managers team. 
#Method: 
#display_manager_info(): Displays the manager and  department, team size, and all information related to the employee and the person. 

class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
    
  def display_person_info(self):
    print('Name:',self.name)
    print('Age:',self.age)  
    
class Employee(Person):
  def __init__(self,name,age,employee_id,salary):
    super().__init__(name,age)
    self.employee_id=employee_id
    self.salary=salary
  
  def display_employee_info(self):
    self.display_person_info()
    print('Employee ID:',self.employee_id)  
    print('Salary:',self.salary)    
        
class Manager(Employee):
     def __init__(self,name,age,employee_id,salary,department,team_size):
        super().__init__(name,age,employee_id,salary)
        self.department=department
        self.team_size=team_size
     def display_manager_info(self):
        self.display_employee_info()
        print('Department:',self.department)
        print('Team Size:',self.team_size)
        
Manager1=Manager('Prajakta','20','2001',100000,'IT',5)     
Manager1.display_manager_info()
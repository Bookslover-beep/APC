#12.Create a directory structure for a library application with separate packages for: a) Books  
#b)Members  
#c)Transactions  
#Each package should contain suitable modules and a main program should combine all functionality. 


from books import catalog
from members import record
from transactions import issue

print("Books:", catalog.list_books())
print("Members:", record.list_members())
print(issue.issue_book("Python", "Prajakta"))
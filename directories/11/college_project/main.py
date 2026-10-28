#11. Create the following directory structure:  
#a)college_project/ 
#b)main.py 
#c)student/ 
#d)__init__.py 
#e)details.py 
#f)marks.py 
#g)faculty/ 
#h)__init__.py 
#i)details.py 
#Write a program that imports functions from both packages and displays student and faculty information. 


from student import details as student_details
from faculty import details as faculty_details

print(student_details.get_student_info())
print(faculty_details.get_faculty_info())
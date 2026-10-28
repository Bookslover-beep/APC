#2.Create a module student.py containing functions to calculate total marks, percentage, and grade. 
#Import the module into another Python program and generate a student's result. 

import student

marks_list = [85, 90, 78, 92, 88]
tot = student.total_marks(marks_list)
pct = student.percentage(marks_list)
grd = student.grade(pct)

print("Total Marks:", tot)
print("Percentage:", pct)
print("Grade:", grd)
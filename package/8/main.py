#8.Create a package student containing: 
#a)marks.py – total and percentage  
#b)grade.py – grade calculation  
#c)attendance.py – attendance eligibility  
#Write a main program that uses all three modules to generate a student report. 


from student import marks, grade, attendance

m = [85, 90, 80]
tot = marks.total(m)
pct = marks.percentage(m)

print("Total:", tot)
print("Percentage:", pct)
print("Grade:", grade.calculate_grade(pct))
print("Eligible:", attendance.check_eligibility(78))
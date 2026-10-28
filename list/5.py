#5.Create a list of student names. Remove:
#a.First student
#b.Last student
#c.A specific student by name
#Display the remaining list.

stu_name = ["Prajakta", "Sakshi", "Amruta", "Vaishanvi", "Ragini"]
print("Original List:",stu_name)
stu_name.pop(0)
stu_name.pop()
stu_name.remove("Vaishanvi")
print("Updated List:",stu_name)
#16.Create a nested list storing:
#a.Student Name b.Roll Number c.Marks
#Display all student details.
students = [
    ["Amruta", 101, 90],
    ["Ragini", 102, 87],
    ["Sakshi", 103, 95]
]
print("students =",students)
print()
print("Student Details:")
for student in students:
    print(f"Name: {student[0]}  Roll No: {student[1]}  Marks: {student[2]}")
#47.Take a list of tuples containing student names and marks, sort the students according to their marks using lambda.

sort_students = lambda students: sorted(students, key=lambda x: x[1])

n = int(input("Enter number of students: "))
student_list = []
for _ in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    student_list.append((name, marks))

print("Students sorted by marks:", sort_students(student_list))
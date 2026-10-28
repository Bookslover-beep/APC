#49.Take a list containing student names and marks, use functions and lambda expressions to:
#a)Calculate average marks. 
#b)Filter students scoring above 75. 
#c)Sort students according to marks.

calc_average = lambda students: sum(marks for _, marks in students) / len(students) if students else 0
filter_above_75 = lambda students: list(filter(lambda x: x[1] > 75, students))

sort_by_marks = lambda students: sorted(students, key=lambda x: x[1], reverse=True)

n = int(input("Enter total number of students: "))
students_data = []

for _ in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students_data.append((name, marks))

if students_data:
    print("\n--- Student Records Analysis ---")
    print(f"Average Marks = {calc_average(students_data):.2f}")
    print(f"Students Scoring Above 75 = {filter_above_75(students_data)}")
    print(f"Students Sorted by Marks (Descending) = {sort_by_marks(students_data)}")
else:
    print("No student data provided.")
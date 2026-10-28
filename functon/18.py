#18.Create a function that accepts marks in five subjects and returns the student's percentage and grade.

def student_report(marks):
    total = sum(marks)
    percentage = total / len(marks)
    if percentage >= 85:
        grade = 'A'
    elif percentage >= 70:
        grade = 'B'
    elif percentage >= 50:
        grade = 'C'
    else:
        grade = 'F'
    return percentage, grade

marks_input = list(map(float, input("Enter marks for 5 subjects separated by spaces: ").split()))
pct, grd = student_report(marks_input)
print(f"Percentage = {pct:.2f}%, Grade = {grd}")
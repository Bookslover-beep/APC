#23.Write a program using separate functions to process student records containing name, roll number, and marks in five subjects. Calculate total, percentage, grade, class average, highest scorer, and lowest scorer.

def process_students(students_data):
    results = []
    total_class_marks = 0
    highest = -1
    lowest = float('inf')
    high_scorer = low_scorer = ""
    
    for name, roll, marks in students_data:
        tot = sum(marks)
        pct = tot / len(marks)
        total_class_marks += tot
        if tot > highest:
            highest = tot
            high_scorer = name
        if tot < lowest:
            lowest = tot
            low_scorer = name
        results.append((name, roll, tot, pct))
        
    class_avg = total_class_marks / len(students_data) if students_data else 0
    return results, class_avg, high_scorer, low_scorer

num_students = int(input("Enter number of students: "))
students_data = []

for _ in range(num_students):
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = list(map(float, input("Enter marks for 5 subjects separated by spaces: ").split()))
    students_data.append((name, roll, marks))

if students_data:
    results, class_avg, high_scorer, low_scorer = process_students(students_data)

    print("\n--- Individual Student Reports ---")
    for name, roll, tot, pct in results:
        print(f"Name: {name} | Roll: {roll} | Total Marks: {tot} | Percentage: {pct:.2f}%")

    print("\n--- Class Summary ---")
    print(f"Class Average Total Marks: {class_avg:.2f}")
    print(f"Highest Scorer: {high_scorer}")
    print(f"Lowest Scorer: {low_scorer}")
else:
    print("No student data provided.")
#17.Create a file containing student records in the format: 
#RollNo,Name,Marks 
#101,Amit,85 
#102,Priya,92 
#103,Rahul,78 
#Write a program to: 
#•Display all records.  
#•Find the student with the highest marks.  
#•Calculate average marks.  
#•Display students who scored more than 80. 


with open("records.txt", "w") as f:
    f.write("RollNo, Name, Marks\n")
    f.write("101, Amit, 85\n")
    f.write("102, Priya, 92\n")
    f.write("103, Rahul, 78\n")

with open("records.txt", "r") as f:
    lines = f.readlines()[1:]
    records = []
    total_marks = 0
    highest_marks = -1
    top_student = ""
    for line in lines:
        parts = [p.strip() for p in line.split(",")]
        roll, name, marks = int(parts[0]), parts[1], float(parts[2])
        records.append((roll, name, marks))
        total_marks += marks
        if marks > highest_marks:
            highest_marks = marks
            top_student = name

    print("All Records:", records)
    print("Highest Marks Student:", top_student, highest_marks)
    print("Average Marks:", total_marks / len(records))
    print("Scored > 80:")
    for roll, name, marks in records:
        if marks > 80:
            print(name, marks)
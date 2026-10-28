#1.Write a Python program to create a file named student.txt and write the student's name, roll number, branch, and semester into the file. 

with open("student.txt", "w") as f:
    f.write("Name: Prajakta Magar\n")
    f.write("Roll Number: 14\n")
    f.write("Branch: CSE\n")
    f.write("Semester: 5\n")
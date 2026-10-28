#8.Write a program to read a text file and display its lines in reverse order. 

with open("student.txt", "r") as f:
    lines = f.readlines()
    for line in reversed(lines):
        print(line, end="")
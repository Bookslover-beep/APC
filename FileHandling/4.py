#4.Write a program to read a text file line by line and display each line separately. 

with open("student.txt", "r") as f:
    for line in f:
        print(line, end="")
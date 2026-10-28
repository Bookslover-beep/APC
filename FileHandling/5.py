#5.Write a program to count and display the total number of lines present in a text file. 

with open("student.txt", "r") as f:
    lines = f.readlines()
    print("Total lines:", len(lines))
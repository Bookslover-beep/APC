#3.Write a program to append additional student information to an existing file without deleting its previous contents. 

with open("student.txt", "a") as f:
    f.write("Email: john@example.com\n")
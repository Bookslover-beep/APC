#16.Read a text file and create another file containing the same text in uppercase. 

with open("student.txt", "r") as src, open("upper.txt", "w") as dest:
    dest.write(src.read().upper())
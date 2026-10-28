#6.Write a program to count the total number of words present in a text file. 

with open("student.txt", "r") as f:
    text = f.read()
    words = text.split()
    print("Total words:", len(words))
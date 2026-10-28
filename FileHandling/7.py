#7.Write a program to count the total number of characters in a text file, including spaces. 

with open("student.txt", "r") as f:
    text = f.read()
    print("Total characters:", len(text))
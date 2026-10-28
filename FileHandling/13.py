#13.Accept a word from the user and search for it in a text file. Display the number of occurrences and the line numbers where it appears. 

target = input("Enter word to search: ")
occurrences = 0
line_numbers = []
with open("student.txt", "r") as f:
    for idx, line in enumerate(f, 1):
        words = line.split()
        if target in words:
            occurrences += words.count(target)
            line_numbers.append(idx)
print("Occurrences:", occurrences)
print("Line numbers:", line_numbers)
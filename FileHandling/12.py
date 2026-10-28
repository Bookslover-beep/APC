#12.Read a text file and count how many times each word occurs. Display the result using a dictionary. 

with open("student.txt", "r") as f:
    words = f.read().split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    print(word_count)
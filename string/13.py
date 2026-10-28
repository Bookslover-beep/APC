#Find the shortest word in a sentence. 
s = input("Enter any sentence: ")
words = s.split()
shortest = words[0]
for word in words:
    if len(word) < len(shortest):
        shortest = word
print(shortest)

#Count how many times a specific word appears in a sentence. 
s = input("Enter any sentence: ")
word = input("Enter any word: ")
count = 0
for x in s.split():
    if x == word:
        count += 1
print(count)
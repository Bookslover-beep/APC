#Find the longest word in a given sentence. 
s = input("Enter any sentence: ")
words = s.split()
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print(longest)
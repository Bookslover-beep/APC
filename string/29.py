#Reverse the order of words in a sentence without changing the words themselves. 
#Example:
#Input: Python is easy
#Output: easy is Python
s = input("Enter any sentence: ")
words = s.split()
result = ""
i = len(words) - 1
while i >= 0:
    result += words[i] + " "
    i -= 1
print(result.strip())
#Find the character with the highest frequency. 
s = input("Enter the string: ")
max_count = 0
result = ""
for ch in s:
    if s.count(ch) > max_count:
        max_count = s.count(ch)
        result = ch
print(result)

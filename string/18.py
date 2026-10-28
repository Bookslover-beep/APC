#Remove duplicate characters while maintaining the original order. 
s = input("Enter a string: ")
result = ""
for char in s:
    if char not in result:
        result += char
print(result)
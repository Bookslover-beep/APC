#Print all duplicate characters in a string
s = input("Enter a string: ")
result = ""
for ch in s:
    if s.count(ch) > 1 and ch not in result:
        result += ch
print(result)


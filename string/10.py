#Display each character of a string along with its ASCII value
s = input("Enter a string: ")
for char in s:
    print(char, ord(char))
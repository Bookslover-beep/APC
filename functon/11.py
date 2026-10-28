#11.Write a function that accepts a string and returns its reverse.

def reverse_string(s):
    return s[::-1]

text = input("Enter a string: ")
print(f"Reversed string = {reverse_string(text)}")
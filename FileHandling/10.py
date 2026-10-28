#10.Read a text file and calculate the number of alphabets, digits, spaces, and special characters. 

with open("student.txt", "r") as f:
    text = f.read()
    alphabets = digits = spaces = specials = 0
    for char in text:
        if char.isalpha():
            alphabets += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1
        else:
            specials += 1
    print("Alphabets:", alphabets)
    print("Digits:", digits)
    print("Spaces:", spaces)
    print("Special characters:", specials)
#10.Define a function that accepts a string and returns the number of vowels present in it.

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

text = input("Enter a string: ")
print(f"Number of vowels = {count_vowels(text)}")
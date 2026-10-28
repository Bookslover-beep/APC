#12.Create a function that checks whether a given string or number is a palindrome.

def is_palindrome(val):
    s = str(val)
    return s == s[::-1]

user_val = input("Enter a string or number: ")
if is_palindrome(user_val):
    print(f"'{user_val}' is a palindrome.")
else:
    print(f"'{user_val}' is not a palindrome.")
#31.Check whether a string is a palindrome using recursion.

def recursive_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return recursive_palindrome(s[1:-1])

text = input("Enter a string to check for palindrome: ").strip()
if recursive_palindrome(text):
    print(f"'{text}' is a palindrome.")
else:
    print(f"'{text}' is not a palindrome.")
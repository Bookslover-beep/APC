#4.Create a module string_utils.py containing functions to count vowels, reverse a string, check palindrome, count words, and remove spaces. 

import string_utils

text = "madam racecar"
print("Vowels:", string_utils.count_vowels(text))
print("Reversed:", string_utils.reverse_string(text))
print("Palindrome:", string_utils.check_palindrome(text))
print("Word count:", string_utils.count_words(text))
print("Without spaces:", string_utils.remove_spaces(text))
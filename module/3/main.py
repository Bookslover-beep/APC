#3.Create a module number_utils.py containing functions to check whether a number is prime, palindrome, Armstrong, or perfect. 
#Import the required functions into a main program. 

from number_utils import is_prime, is_palindrome, is_armstrong, is_perfect

num = 153
print("Prime:", is_prime(num))
print("Palindrome:", is_palindrome(num))
print("Armstrong:", is_armstrong(num))
print("Perfect:", is_perfect(num))
#7.Create a package named mathutils containing: 
#a)basic.py – arithmetic operations  
#b)number.py – prime, Armstrong, palindrome functions  
#c)statistics.py – mean, maximum, minimum  
#Create a main program that imports functions from each module. 

from mathutils import basic, number, statistics

print("Add:", basic.add(5, 3))
print("Prime:", number.is_prime(7))
print("Mean:", statistics.mean([1, 2, 3, 4, 5]))
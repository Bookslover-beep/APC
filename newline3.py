#Three Problem Statement

#1.Write a python program to print sentences and new line in python
print("Welcome to learning Advanced Python\nPython is a case-sensitive language")
print()
print("Hello")
print("World")
print()
print("Hello")
print()
print("World")
print()

print('''Hello
World!''')
print()
print("Hello","world",sep="\n")
print()
print("Hello",end="\n")
print("World")
print()

#2.Write a program to sawp to number without using third no. in python
a = int(input("Enter a value of a:"))
b = int(input("Enter a value of b:"))
a, b=b, a
print("a=",a)
print("b=",b)
print()

c = 10
d = 20
temp = c
c = d 
d = temp
print("c=",c)
print("d=",d)
print()

#3.Write a program of factorialof given no.
print("Factorial")
num=int(input("Enter a number:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(f"Factorial of {num} is",fact) 
print()

#4.fibonnacci
print("fibonnacci")
def fibonacci(n):
 d, e=0, 1
 for i in range(n):
     print(d, end=' ')
     d, e = e,d + e
num = int(input("Enter the number of terms: "))
fibonacci(num)




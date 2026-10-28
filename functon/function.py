#Functions
def input(n1, n2):
    print("number 1 is ", n1)
    print("number 2 is ", n2)
print("Call to function...")
input(50,30)

#function without parameters
def greet():
    print("Hello, World!")
greet()
print()

#function with parameters
def greet_person(name):
    print(f"Hello, {name}!")
greet_person("Alice")
print()

#default arguments in function
def function(n1, n2 = 20):
    print("number 1 is: ", n1)
    print("number 2 is: ", n2)
print("Passing one argument...")
function(40)
print("Passing two arguments...")
function(50,30)
print()

#lambda function
print("Applying lambda function...")
def add(num):
    return num+4
print(add(6))
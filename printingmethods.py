#All Printing methods

name ="Prajakta"
print(f"name = {name}")
print(type(name))
print()

age=20
print(f"age = {age}")
print(type(age))
print()

#1.Using print()
print("Using print()")
print("My name is",name,"and age is",age)
print()

#2.Using format()
print("Using format()")
print("My name is {} and age is {}".format(name, age))
print()

#3.Using sep and end parameter
print("Using sep and end parameter")
print("Python",end="@")
print("Programming")
print('G','F','G',sep='')
print()

#4.Using f-string
print("Using f-string")
print(f"My name is {name} and age is {age}")
print()

#5.Using % operator
print("Using % operator")
print("My name is %s and age is %d" % (name, age))


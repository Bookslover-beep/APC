#Set
print("Example: Set using curly braces")
days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
print(days)
print(type(days))
print()

print("Looping through set elements: ")
for i in days:
    print(i)
print()

print("Example: Set using set() function")
days = set({"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"})
print(days)
print()

print("Looping through set elements: ")
for i in days:
    print(i)
print()

#adding elements to set
print("Adding elements to set...")
months = set({"January", "February", "March", "April", "May", "June"})
print("Original set: ")
print(months)
print("Added month... ")
months.add("October")
print("Updated set: ")
print(months)
print()

#adding elements to set
print("Adding elements to set using update()...")
months = set({"January", "February", "March", "April", "May", "June"})
print("Original set: ")
print(months)
months.update({"July", "August", "September", "October"})
print("Updated set: ")
print(months)
print()

#removing elements to set
print("removing elements to set using set()...")
months = set({"January", "February", "March", "April", "May", "June"})
print("Original set: ")
print(months)
print()
print("removing months... ")
print()
months.discard("January")
print("Modified set: ")
print(months)
print("looping through set elements...")
for i in months:
    print(i)

#second method
months.remove("February")
months.remove("March")
print("Modified set: ")
print(months)
print()

#third method
months = set({"January", "February", "March", "April", "May", "June"})
print("Original set: ")
print(months)
print()
print("removing all months... ")
print()
months.clear()
print(months)
print()

#Union Operation
print("Applying Union Operation...")
d1 = {"Monday", "Tuesday", "Wednesday", "Thursday", "Sunday"}
d2 = {"Friday", "Saturday", "Sunday"}
print(d1|d2)

#Intersection 
#intersection Operation
print("Applying insertion Operation...")
d1 = {"Monday", "Tuesday", "Wednesday", "Thursday", "Sunday"}
d2 = {"Friday", "Saturday", "Sunday"}
print(d1&d2)
print()

























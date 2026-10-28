#Statements

#Break Statement
print("Break Statement")
for string in "Python Loops":
 if string=='L':
  break
 print("Current letter:",string)
print()

#Continue
print("Continue Statement")
for string in "Python Loops":
 if string=='o' or string== 'p' or string=='t':
  continue
 print("Current letter:",string)
print()

#Pass Statement
print("Pass Statement")
def pass_example():
 for i in range(0,10):
  pass
 print("Good Bye!")
pass_example()
print()

#multiline string
print("Multiline string")
a="""Welcome
DYPCET
2026 BATCH"""
print(a)
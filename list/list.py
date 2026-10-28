# A simple List
list1 = [1,2,"Python","Programming",15.9]
list2 = ["Amy","Ryan","Emma"]
print("Simple List")
print("list1 = ",list1)
print("list2 = ",list2)
print()
print(type(list1))
print(type(list2))
print()
print(id(list1))
print(id(list2))
print()

#mutable or immutable
l=[1,2,3,"Hello World"]
print(l)
print(type(l))
print("Id od list",id(l))
l.append(4)
print(l)
print(id(l))
print()


#+ve Indexing lists
print("Positive Indexing Lists")
l = [0, 1, 2, 3, 4, 5]
print(l[0:])
print(l[:])
print(l[2:4])
print(l[1:3])
print(l[:4])
print()

#-ve Indexing lists
print("Negative Indexing Lists")
l = [0, 1, 2, 3, 4, 5]
print(l[-1:-5])
print(l[-3:])
print(l[:-1])
print(l[3:-1])
print()

#Iterating a list
print("Iterative list")
list = ["john","David","James","Jonathan"]
for i in list:
    print(i)
print()

#append and insert method
print("Append and Insert Method")
I=[]
n = int(input("Enter how many items you want to add:"))
for i in range(0,n):
    I.append(input("Enter the item:"))
print()
print("printing the list items:")
for i in I:
    print(i,end=" ") 
print()

#Removing element from the list
print("\nRemove element from the list")
list = [0,1,2,3,4]
print("Printing original list:")
for i in list:
    print(i,end=" ")
list.remove(2)
print("\nPrinting the list after the removal of first element")
for i in list:
    print(i,end=" ")
print()

#Concatenation two lists
print("\nConcatenation two lists")
list1 = [12,14,16,18,20]
list2 = [9,10,32,54,86]
print("list1 =",list1)
print("list2 =",list2)
l = list1 + list2
print("l =",l)
print()

#Repetiiton of list
print("Repetition of list")
l1 = [12,14,16,18,20]
print("l1 =",l1)
l = l1 * 2
print("l = ",l)
print()

#List Methods
print("\nList Methods:")
l=[10, 30, 20, 50, 40, 60]
print("List:",l)
print("Type of an object:", type(l))
l.append(70)
print("\n70 is appended: ", l)
l.insert(2, 90)
print("\n90 is inserted: ", l)
l1=[100, 300, 400, 900]
l.extend(l1)
print("\nExtended list: ", l)
l.sort()
print("\nSorted list: ", l)
l.reverse()
print("\nReversed list: ", l)
l2=l.copy()
print("\nCopied list: ", l2)
l.pop()
print("\nList after popping single element: ", l)
l.remove(900)
print("\n900 removed: ", l)
l.append(900)
print("\nAppended list: ", l)
l.clear()
print("\nClear method:",l)
print()



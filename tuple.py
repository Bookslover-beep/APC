#Tuple
t1=(4,"python",9.3)
print("Tuple with different data types:",t1)

#Immutable
t1 = (1,2,3,"Python")
print("t1 =",t1)
print(type(t1))
print(id(t1))
print()
t2 = ("java","Hello World",12,15,20)
print("t2 =",t2)
print(type(t2))
print(id(t2))

#Convert tuple into mutable
tuple = (10, 20, 30)
print("Original:", tuple)
print("Type:", type(tuple))
print("Memory Address:", id(tuple))
print("Converting to Mutable...")
mutable_list = list(tuple)
mutable_list[0] = 99
print("Updated List:", mutable_list)
print("Type:", type(mutable_list))
print("Memory Address:", id(mutable_list))

t = t1 + t2
print("t = ",t)
print(type(t))
print(id(t))

#count() method
print("count method")
t1 = (0,1,5,6,7,2,2,4,2,3,2,3,1,3,2)
print("t1 = ",t1)
t2 = ("Python","java","Python","Tpoint","Python","java")
print("t2 = ",t2)
res = t1.count(2)
print("Count of 2 in T1 is:",res)
print()

#Count() method: tuple
t1=(0, 1, 5, 6, 7, 2, 2, 4, 2, 3, 2, 3, 1, 3, 2)
print("t1 = ",t1)
print(type(t1))
t2=('Python', 'Java', 'Python', 'Tpoint', 'Python', 'Java')
print("t2 = ",t2)
print(type(t2))
res=t1.count(2)
print("Count of 2 in T1 is: ", res)
res1=t2.count('Java')
res2=t2.count('Python')
print("Count of Java in T2 is: ", res1)
print("Count of Python in T2 is: ", res2)
print()
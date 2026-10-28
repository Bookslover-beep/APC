#creating array
import array as arr
a = arr.array('i', [1,2,3])
print("newly created array: ", end=" ")
for i in range (0,3):
    print(a[i], end=" ")
print()
b = arr.array('d', [2.5, 3.2, 3.3])
print("newly created array: ", end=" ")
for i in range(0,3):
    print(b[i], end=" ")

#inserting in array
import array as arr
a = arr.array('i', [1,2,3])
print("newly created array: ", end=" ")
for i in range (0,3):
    print(a[i], end=" ")
print()
a.insert(1,4)
print("Array after insertion: ", end=" ")
for i in range (0,4):
    print(a[i], end=" ")

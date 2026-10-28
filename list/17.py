#17.Create two 3 × 3 matrices using nested lists and perform matrix addition.
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
print("matrix1 =",matrix1)
print("matrix2 =",matrix2)
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

for row in result:
    print(row)
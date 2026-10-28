#24.Rotate a list:
#a.Left by one position b.Right by one position
numbers = [1, 2, 3, 4, 5]
print("numbers =",numbers)

left_rotated = numbers[1:] + numbers[:1]
right_rotated = numbers[-1:] + numbers[:-1]

print("Left rotated by 1:", left_rotated)
print("Right rotated by 1:", right_rotated)
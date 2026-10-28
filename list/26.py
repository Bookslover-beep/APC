#26.Store marks of 20 students in a list and determine:
#a.Highest marks b.Lowest marks c.Average marks
#d.Number of students scoring above average e.Number of students scoring below average

marks = [85, 72, 90, 45, 60, 88, 95, 50, 67, 73, 81, 39, 92, 58, 64, 77, 83, 49, 91, 68]
print("marks =",marks)

highest = max(marks)
lowest = min(marks)
avg = sum(marks) / len(marks)

above_avg = sum(1 for m in marks if m > avg)
below_avg = sum(1 for m in marks if m < avg)

print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Average marks:", avg)
print("Students above average:", above_avg)
print("Students below average:", below_avg)
#7.Accept 10 numbers from the user and store them in a list. Calculate:
#a.Sum
#b.Average

numbers = []
for i in range(10):
    n = int(input(f"Enter number {i + 1}: "))
    numbers.append(n)
print("numbers =",numbers)
total_sum = sum(numbers)
average = total_sum / 10

print("Sum:", total_sum)
print("Average:", average)
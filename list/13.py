#13.Accept 10 numbers and sort them in:
#a.Ascending order b.Descending order
num = []

for i in range(10):
    n = int(input(f"Enter number {i+1}: "))
    num.append(n)
print("num =",num) 
ascending = sorted(num)
descending = sorted(num, reverse=True)

print("Ascending order:", ascending)
print("Descending order:", descending)
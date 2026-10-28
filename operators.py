# Python Operator
a = 10
b = 3

# 1. Arithmetic Operators
print("1. Arithmetic Operators")
print("Addition (+):", a + b)
print("Subtraction (-):", a - b)
print("Multiplication (*):", a * b)
print("Division (/):", a / b)
print("Floor Division (//):", a // b)
print("Modulus (%):", a % b)
print("Exponent (**):", a ** b)

# 2. Comparison Operators
print("\n2. Comparison Operators")
print("Equal to (==):", a == b)
print("Not equal to (!=):", a != b)
print("Greater than (>):", a > b)
print("Less than (<):", a < b)
print("Greater than or equal to (>=):", a >= b)
print("Less than or equal to (<=):", a <= b)

# 3. Assignment Operators
print("\n3. Assignment Operators")
x = 10
print("x =", x)
x += 5
print("x += 5:", x)
x -= 3
print("x -= 3:", x)
x *= 2
print("x *= 2:", x)
x /= 4
print("x /= 4:", x)
x //= 2
print("x //= 2:", x)
x %= 3
print("x %= 3:", x)
x **= 2
print("x **= 2:", x)

# 4. Logical Operators
print("\n4. Logical Operators")
p = True
q = False

print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)

# 5. Bitwise Operators
print("\n5. Bitwise Operators")
m = 5      # Binary: 101
n = 3      # Binary: 011
print("m & n (AND):", m & n)
print("m | n (OR):", m | n)
print("m ^ n (XOR):", m ^ n)
print("~m (NOT):", ~m)
print("m << 1 (Left Shift):", m << 1)
print("m >> 1 (Right Shift):", m >> 1)

# 6. Membership Operators
print("\n6. Membership Operators")
numbers = [10, 20, 30, 40]
print("20 in numbers:", 20 in numbers)
print("50 in numbers:", 50 in numbers)
print("20 not in numbers:", 20 not in numbers)
print("50 not in numbers:", 50 not in numbers)

# 7. Identity Operators
print("\n7. Identity Operators")
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]
print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)
print("list1 is not list3:", list1 is not list3)


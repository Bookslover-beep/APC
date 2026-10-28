#File Handling 

# Reading and writing in the file
file = open("report.txt", "w+")
print("Writing in the file")
print() 

while True:
    line = input("Enter a sentence: ")
    file.write(line)
    file.write('\n')
    choice = input("Do you wish to enter more data? (y/n): ")
    if choice in ('n', 'N'): 
        break

print("The byte position of file object is", file.tell())
file.seek(0) 
print()
print("File contains (Reading from file):")
content = file.read()
print(content)
file.close()


# 1. Read - r
print("\n--- 1. Read ---")
file = open("report.txt", "r")
data = file.read()
print(data)
file.close()


# 2. Write - w
print("\n--- 2. Write ---")
file = open("report.txt", "w")
line = input("Enter text to write: ")
file.write(line)
file.close()


# 3. Append - a
print("\n--- 3. Append ---")
file = open("report.txt", "a")
line = input("Enter text to append: ")
file.write("\n" + line)
file.close()


# 4. Read + Write - r+
print("\n--- 4. Read + Write (r+) ---")
file = open("report.txt", "r+")
line = input("Enter text: ")
file.write(line)
file.seek(0)
data = file.read()
print("File content:", data)
file.close()


# 5. Write + Read - w+
print("\n--- 5. Write + Read (w+) ---")
file = open("report.txt", "w+")
line = input("Enter text: ")
file.write(line)
file.seek(0)
data = file.read()
print("File content:", data)
file.close()


# 6. Append + Read - a+
print("\n--- 6. Append + Read (a+) ---")
file = open("report.txt", "a+")
line = input("Enter text to append: ")
file.write("\n" + line)
file.seek(0)
data = file.read()
print("File content:", data)
file.close()


# 7. Create new file (empty file) - x
print("\n--- 7. Create new empty file (x) ---")
try:
    file = open("new_report.txt", "x")
    file.write("This is a newly created file.")
    file.close()
    print("new_report.txt created successfully.")
except FileExistsError:
    print("new_report.txt already exists.")


# 8. Read Binary - rb
print("\n--- 8. Read Binary (rb) ---")
file = open("report.txt", "rb")
data = file.read()
print(data)
file.close()


# 9. Write Binary - wb
print("\n--- 9. Write Binary (wb) ---")
file = open("binary_report.txt", "wb")
data = input("Enter text for binary file: ")
file.write(data.encode())
file.close()


# 10. Append Binary - ab
print("\n--- 10. Append Binary (ab) ---")
file = open("binary_report.txt", "ab")
data = input("Enter text to append to binary file: ")
file.write(("\n" + data).encode())
file.close()


# Test tell() and seek()
print("\n--- Test tell() and seek() ---")
f = open("report.txt", "r")
print("Initial position:", f.tell())       
f.seek(5)                
print("Position after seek(5):", f.tell())       
f.close()

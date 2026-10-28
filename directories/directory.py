# Directory 

import os

# 1. Working directory
print("\nWorking directory",os.getcwd())

#2. List directory
print("\nList directory",os.listdir())

#3. Create directory
print("\nCreate directory")
if not os.path.exists("myfolder"):
    os.mkdir("myfolder")
    print("Directory created")
else:
    print("Directory already exists")

# 4. Rename file
print("\nrename file")
os.rename("new1_report.txt", "new_report.txt")


# 5. Change Path 
print("\n Change Directory")
os.chdir(r"C:\Users\LENOVO\Documents\APC\labexp\directories")
print("Current directory",)

# 6 Delete folder
print("\n Delete empty folder")
os.rmdir("myfolder")



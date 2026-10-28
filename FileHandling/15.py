#15.Read a Python source file and create another file after removing single-line comments. 

with open("15.py", "r") as src, open("cleaned.py", "w") as dest:
    for line in src:
        if not line.strip().startswith("#"):
            dest.write(line)
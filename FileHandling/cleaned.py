
with open("15.py", "r") as src, open("cleaned.py", "w") as dest:
    for line in src:
        if not line.strip().startswith("#"):
            dest.write(line)
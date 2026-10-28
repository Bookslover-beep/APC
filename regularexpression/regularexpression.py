# Regular Expression

import re

text = "prajakta1811@gmail.com"

# 1. findall()
result = re.findall(r"\w+", text)
print("Findall:", result)


# 2. compile()
pattern = re.compile(r"\w+@\w+\.\w+")
result = pattern.search(text)
print("Compile:", result.group())


# 3. split()
split = re.split(r"@", text)
print("Split:", split)


# 4. sub()
sub = re.sub(r"gmail", "yahoo", text)
print("Sub:", sub)


# 5. escape()
esc = re.escape(text)
print("Escape:", esc)


# 6. search()
result = re.search(r"\w+@\w+\.\w+", text)

if result:
    print("Search:", result.group())
else:
    print("Search: No match")
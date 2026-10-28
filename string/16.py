#Display the frequency of every character in a string
s = input("Enter a string: ")
done = ""
for ch in s:
    if ch not in done:
        print(ch, s.count(ch))
        done += ch
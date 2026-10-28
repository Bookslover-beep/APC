#Find the second most frequently occurring character. 
s = input("Enter the string: ")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
values = sorted(set(freq.values()), reverse=True)
for ch in s:
    if freq[ch] == values[1]:
        print(ch)
        break
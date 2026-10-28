#46.Take a list of words; sort them according to their length using lambda.

sort_words_by_len = lambda lst: sorted(lst, key=lambda w: len(w))

words = input("Enter words separated by spaces: ").split()
print("Words sorted by length =", sort_words_by_len(words))
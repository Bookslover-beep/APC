#45.Take a list of words, use filter() and lambda to find words having more than five characters.

filter_long_words = lambda lst: list(filter(lambda w: len(w) > 5, lst))

words = input("Enter words separated by spaces: ").split()
print("Words with > 5 characters =", filter_long_words(words))
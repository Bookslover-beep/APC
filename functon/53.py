#52.Write a program using functions, map(), filter(), and lambda expressions to process a list of words and:
#a)Find the length of every word. 
#b)Extract words having more than five characters. 
#c)Sort words according to their length.

get_lengths = lambda words: list(map(lambda w: (w, len(w)), words))
filter_long_words = lambda words: list(filter(lambda w: len(w) > 5, words))
sort_words_len = lambda words: sorted(words, key=lambda w: len(w))

words = input("Enter words separated by spaces: ").split()

if words:
    print("\n--- Word Processing Results ---")
    print("Length of every word:", get_lengths(words))
    print("Words with more than 5 characters:", filter_long_words(words))
    print("Words sorted according to length:", sort_words_len(words))
else:
    print("No words provided.")
#10. Create a package texttools containing: 
#a)cleaning.py – remove punctuation and extra spaces  
#b)tokenization.py – tokenize text  
#c)frequency.py – word-frequency analysis Create a main program to use the package. 


from texttools import cleaning, tokenization, frequency

text = "  hello world hello python  "
cleaned = cleaning.remove_extra_spaces(text)
tokens = tokenization.tokenize(cleaned)
print("Frequency:", frequency.word_frequency(tokens))
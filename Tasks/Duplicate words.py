from string import punctuation
from collections import Counter
text = """\I am name i am Name I name i mine hello if my name is hello is my name is hello"""
text = open("file.txt").read()
text2 = ''.join(c for c in text.lower() if c not in punctuation)
word_list = text2.split()
duplicate_word_list = sorted(Counter(word_list) - Counter(set(word_list)))
print("Original text:")
print(text)
print('-'*72)
print("A list of duplicate words in the text:")
print(duplicate_word_list)

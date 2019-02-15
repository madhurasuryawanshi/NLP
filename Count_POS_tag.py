from collections import Counter
import nltk
text = " Guru99 is one of the best sites to learn WEB, SAP, Ethical Hacking and much more online."
lower_case = text.lower()
tokens = nltk.word_tokenize(lower_case)
tags = nltk.pos_tag(tokens)

counts = Counter( tag for word,  tag in tags)
print(counts)
import nltk
text = "Hello Guru99, You have to build a very good site, and I love visiting your site."
sentence = nltk.sent_tokenize(text)
for sent in sentence:
	print(nltk.pos_tag(nltk.word_tokenize(sent)))
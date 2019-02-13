from nltk.corpus import wordnet
syns = wordnet.synsets("dog")

for syn in wordnet.synsets("dog"):
    for l in syn.lemmas():
        print(l.name())

       
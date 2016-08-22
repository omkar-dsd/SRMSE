import nltk
from nltk.corpus import wordnet

syns = wordnet.synsets("program")

# #synset
# print syns[0].name()
# #word
# print syns[0].lemmas()[0].name()
# #definition
# print syns[0].definition()
# #example
# print syns[0].examples()




synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
	for i in syn.lemmas():
		synonyms.append(i.name())
		if i.antonyms():
			antonyms.append(i.antonyms()[0].name())

print synonyms
print antonyms 

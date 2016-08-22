import nltk
from nltk.corpus import wordnet

w1 = wordnet.synset("boat.n.01")
w2 = wordnet.synset("boat.n.01")

print w1.wup_similarity(w2)


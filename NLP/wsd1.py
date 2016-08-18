#This module is for word sense disambiguation. 
#Give 2 sentences with some data.
#give a third sentence and the program will analyse which sentence you are relating to.


import nltk
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer

#enter 2 sentences
sent1 = raw_input("Enter Sentence 1: ")
sent2 = raw_input("Enter Sentence 2: ")


#this function removes the stop words and returns a fresh word tokenised list.
def filteredSentence(sentence):

	lemmatizer = WordNetLemmatizer()   #lemmatizes the words
	ps = PorterStemmer()    #stemmer stems the root of the word.

	stop_words = set(stopwords.words("english"))
	words = word_tokenize(sentence)

	filtered_sentence = []

	for w in words:
        	if w not in stop_words:
                	filtered_sentence.append(lemmatizer.lemmatize(ps.stem(w)))
	return filtered_sentence


filtered_sent1 = []
filtered_sent2 = []

filtered_sent1 = filteredSentence(sent1)
filtered_sent2 = filteredSentence(sent2)



sent3 = raw_input("Enter Query: ")
filtered_sent3 = filteredSentence(sent3)
sent1_count = 0
sent2_count = 0

for i in filtered_sent3:
	for j in filtered_sent1:
		if(i==j):
			sent1_count = sent1_count + 1

	for j in filtered_sent2:
		if(i==j):
			sent2_count = sent2_count + 1


if(sent1_count>sent2_count):
	print "first"
else:
	print "second"





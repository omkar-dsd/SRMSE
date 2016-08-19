#This module is for word sense disambiguation. 
#Give 2 sentences with some data.
#give a third sentence and the program will analyse which sentence you are relating to.


import nltk, thread
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer

#enter 2 sentences
sent1 = raw_input("Enter Sentence 1: ")
sent2 = raw_input("Enter Sentence 2: ")
sent3 = "start"
while(sent3 != "end"):
	sent3 = raw_input("Enter Query: ")

	#-----------------------------------------------------------------------------------

	#this function removes the stop words, stems the words and returns a fresh word tokenised list.
	def filteredSentence(sentence):

		# if storelist is None:
		# 	storelist = []
		filtered_sent = []
		lemmatizer = WordNetLemmatizer()   #lemmatizes the words
		ps = PorterStemmer()    #stemmer stems the root of the word.

		stop_words = set(stopwords.words("english"))
		words = word_tokenize(sentence)

		for w in words:
	        	if w not in stop_words:
	                	filtered_sent.append(lemmatizer.lemmatize(ps.stem(w)))
		return filtered_sent

	#--------------------------------------------------------------------------------------



		





	filtered_sent1 = []
	filtered_sent2 = []
	filtered_sent3 = []


	filtered_sent1 = filteredSentence(sent1)
	filtered_sent2 = filteredSentence(sent2)
	filtered_sent3 = filteredSentence(sent3)


	# print filtered_sent1
	# print filtered_sent2
	# print filtered_sent3


	sent1_count = 0
	sent2_count = 0


	for i in filtered_sent3:
		for j in filtered_sent1:
			if(i==j):
				sent1_count = sent1_count + 1

		for j in filtered_sent2:
			if(i==j):
				sent2_count = sent2_count + 1
		#try:
		# 	thread.start_new_thread(matchTokens, (i,filtered_sent1,sent1_count, ))
		# 	thread.start_new_thread(matchTokens, (i,filtered_sent2,sent2_count, ))
		# except:
		# 	print "Error: Thread issues"



	if(sent1_count>sent2_count):
		print "first"
	else:
		print "second"



	#Sentence1: the river bank has water in it and it has fishes trees . lots of water is stored in the banks. boats float in it and animals come and drink water from it.
	#sentence2: the commercial banks are used for finance. all the financial matters are managed by financial banks and they have lots of money, user accounts like salary account and savings account, current account. money can also be withdrawn from this bank.
	#query: from which bank should i withdraw money.

print "Thankyou"
#This module is for word sense disambiguation. 
#Give 2 sentences with some data.
#give a third sentence and the program will analyse which sentence you are relating to.


import nltk, thread
import codecs
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import wordnet

#enter 2 sentences
cricfile = codecs.open("cricketbat.txt", 'r', "utf-8")
sent2 = cricfile.read().lower()
vampirefile = codecs.open("vampirebat.txt", 'r', 'utf-8')
sent1 = vampirefile.read().lower()
sent3 = "start"

# FOR TEST
# sent1 = "the commercial banks are used for finance. all the financial matters are managed by financial banks and they have lots of money, user accounts like salary account and savings account, current account. money can also be withdrawn from this bank."
# sent2 = "the river bank has water in it and it has fishes trees . lots of water is stored in the banks. boats float in it and animals come and drink water from it."
# sent3 = "from which bank should i withdraw money"

while(sent3 != "end"):

	sent3 = raw_input("Enter Query: ").lower()

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
	                	for i in synonymsCreator(w):
	                		filtered_sent.append(i)
		return filtered_sent

	#--------------------------------------------------------------------------------------

	#this function adds synonyms to mthe match list

	def synonymsCreator(word):
		synonyms = []

		for syn in wordnet.synsets(word):
			for i in syn.lemmas():
				synonyms.append(i.name())

		return synonyms

	#---------------------------------------------------------------------------------------
	# this function counts the similarity and returns the float on the scale of 0 to 1

	def simlilarityCheck(word1, word2):


		
		word1 = word1 + ".n.01"
		word2 = word2 + ".n.01"
		try:
			w1 = wordnet.synset(word1)
			w2 = wordnet.synset(word2)

			return w1.wup_similarity(w2)
		
		except:
			return 0

	#-----------------------------------------------------------------------------------------



	def simpleFilter(sentence):
			
		# if storelist is None:
		# 	storelist = []
		filtered_sent = []
		lemmatizer = WordNetLemmatizer()
		stop_words = set(stopwords.words("english"))
		words = word_tokenize(sentence)

		for w in words:
	        	if w not in stop_words:
	                	filtered_sent.append(lemmatizer.lemmatize(w))
	                	# for i in synonymsCreator(w):
	                	# 	filtered_sent.append(i)
		return filtered_sent




	filtered_sent1 = []
	filtered_sent2 = []
	filtered_sent3 = []

	counter1 = 0
	counter2 = 0
	sent31_similarity = 0
	sent32_similarity = 0

	filtered_sent1 = simpleFilter(sent1)
	filtered_sent2 = simpleFilter(sent2)
	filtered_sent3 = simpleFilter(sent3)

	for i in filtered_sent3:
	
		for j in filtered_sent1:
			counter1 = counter1 + 1 
			sent31_similarity = sent31_similarity + simlilarityCheck(i,j)

		for j in filtered_sent2:
			counter2 = counter2 + 1
			sent32_similarity = sent32_similarity + simlilarityCheck(i,j)

	# similarity_avg31 = sent31_similarity/counter1
	# similarity_avg32 = sent32_similarity/counter2

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



	#checker

	# print "sent 1 similarity: ", sent31_similarity
	# print "Sent 2 similarity: ", sent32_similarity
	# # print "Similarity Average 31: ", similarity_avg31
	# # print "Similarity Average 32: ", similarity_avg32
	# print "counter one: ", counter1
	# print "counter two: ", counter2
	# print "sent1 match count : ", sent1_count
	# print "sent2 match count : ", sent2_count 
	# # ---------------------------------------------
    #     WITHOUT SIMILARITY


	if((sent1_count + sent31_similarity)>(sent2_count+sent32_similarity)):
		print "Vampire Bat"
	else:
		print "Cricket Bat"
	

	#---------------------------------------------

	#-----------------------------------------------
	#Sentence1: the river bank has water in it and it has fishes trees . lots of water is stored in the banks. boats float in it and animals come and drink water from it.
	#sentence2: the commercial banks are used for finance. all the financial matters are managed by financial banks and they have lots of money, user accounts like salary account and savings account, current account. money can also be withdrawn from this bank.
	#query: from which bank should i withdraw money.

	#sen1: any of various nocturnal flying mammals of the order Chiroptera, having membranous wings that extend from the forelimbs to the hind limbs or tail and anatomical adaptations for echolocation, by which they navigate and hunt prey. 
	#sen 2: a cricket wooden bat is used for playing criket. it is rectangular in shape and has handle and is made of wood or plastic and is used by cricket players. 
print "Thankyou"
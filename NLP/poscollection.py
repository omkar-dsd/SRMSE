import nltk
from bs4 import BeautifulSoup as bs
# from pymongo import MongoClient
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import sent_tokenize, word_tokenize

import urllib2

# PROXY HANDLER----
def  proxyHandler():
	proxy=urllib2.ProxyHandler({})
	opener=urllib2.build_opener(proxy)
	opener.addheaders=[('User-agent','Mozilla/5.0')]
	urllib2.install_opener(opener)

# PROXY HANDLER END -----------

proxyHandler()

temp = "http://www.thehindu.com/"

def getWebText(urltoopen):
	url = urllib2.urlopen(urltoopen).read()
	soup = bs(url).encode("utf-8")

	ptaglist = soup.find('a')
	# textList = []
	# for i in ptaglist:
	# 	textList.append(i.getText())

	return ptaglist

theHindu = getWebText(temp)
print theHindu

tokens = nltk.word_tokenize(theHindu)
tagged = nltk.pos_tag(tokens)




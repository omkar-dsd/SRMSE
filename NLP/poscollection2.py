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

bsoupFile = urllib2.urlopen("http://fairytalesoftheworld.com/quick-reads/the-monkey-who-was-made-king/")
bsoupHtml = bsoupFile.read()

soup = bs(bsoupHtml, "lxml")

atags = soup.findAll('p')

poslist = []
for i in atags:
	poslist.append(i.getText())

posnew_list = []
for i in poslist:
	word_tokens = nltk.word_tokenize(i)
	taggedpos = nltk.pos_tag(word_tokens)
	for j in taggedpos:
		posnew_list.append(j)

posnew_list = dict(posnew_list)

for key, value in posnew_list.iteritems():
	if(value == 'NNP'):
		print key
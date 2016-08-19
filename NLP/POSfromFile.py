import nltk
import codecs
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import sent_tokenize, word_tokenize

story = codecs.open("monkey.txt", "r", "utf-8")
story_text = story.read()

print story_text

sentence_tokens = nltk.sent_tokenize(story_text)
#print sentence_tokens

pos_list = []

for tokens in sentence_tokens:
	word_tokens = nltk.word_tokenize(tokens)
	taggedpos = nltk.pos_tag(word_tokens)
	for i in taggedpos:
		pos_list.append(i)



print pos_list
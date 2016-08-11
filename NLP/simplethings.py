import nltk
import sys

sentence = "At eight o'cllock on Thursday morning Arthur didn't feel very good."

tokens = nltk.word_tokenize(sentence)

#print tokens

tagged = nltk.pos_tag(tokens)

print tagged[0:6]
#tokenizing the sentence by words.

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize 

sentence = "At eight o'clock on Thursday morning Arthur didn't feel very good."

print (word_tokenize(sentence))
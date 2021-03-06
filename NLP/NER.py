#Named Entity Recognition
#Author: Omkar

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

firstfile = open("testfile.txt","r+")
train_text = firstfile.read()
secondfile = open("testfile2.txt","r+")

sample_text = secondfile.read()

#Below is Sentence tokenizer
#PunktSentenceTokenizer shou be a large file and it is used to create a learning text.
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)
#--------------------------


def process_content():
    try:
        for i in tokenized:
                #tokenizing sentences to words
            words = nltk.word_tokenize(i)
            #pos tagging the tokenized words
            tagged = nltk.pos_tag(words)
            #special regex for chunk
            namedEnt = nltk.ne_chunk(tagged, binary = True)

            namedEnt.draw()

    except Exception as e:
        print(str(e))

process_content()

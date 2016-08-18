import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer


# Train the Machine
# There was once a dog. The dog went up to the hill and jumped down. Cat was walking on the road, and a car came and hit the cat. The cat died. 
# Check:
# There was a tall tree. The tree grew more tall. The treee grew old and beared sweet fruits.


#firstfile = open("testfile.txt","r+")
print "Train the Machine"
train_text = raw_input()
#secondfile = open("testfile2.txt","r+")
print "Check:"
sample_text = raw_input() 

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
            # chunkGram = r"""Chunk: {<.*>+}
            # 				}<VB.?|IN|DT>+{				""" #This is chinking part, which is negation of chunking.
            # #looking for regex pattern using pattern
            # chunkParser = nltk.RegexpParser(chunkGram)
            # #parsing the string
            # chunked = chunkParser.parse(tagged)
            # #drawing sentence
            # chunked.draw()     


    except Exception as e:
        print(str(e))

process_content()
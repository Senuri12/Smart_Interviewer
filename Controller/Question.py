import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.wsd import lesk
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet
wn.synsets('able')
sent = "people should be able to marry a person of their choice"
nltk.wsd.lesk(sent, 'able')
print(nltk.wsd.lesk(sent.split(), 'able').definition())
sent = 'I went to the bank to deposit my money'
ambiguous = 'bank'
print(lesk(sent, ambiguous))
print(lesk(sent, ambiguous).definition())
train_text = state_union.raw("2005-GWBush.txt")
sample_text ="He personal details"

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            # print(tagged)
            namedEnt = nltk.ne_chunk(tagged, binary=True)
            namedEnt.draw()
            print(namedEnt)
            chunkGram = r""" Chunk: {<NE.?>}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(namedEnt)


            # chunked.draw()
            # print(chunked)

    except Exception as e:
        print(str(e))


process_content()




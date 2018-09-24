
import sys

import nltk
import os,glob
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from Controller import vik_test_codes
from Controller  import ConnectionToNeo4j,TextToSpeechConverter,QuestionCreator,NestedQuestionCreator,vari,test,AudioRecorder,SpeachToText

sys.path.insert(0, '../Database')



from Database import TechnicalQuestionDictionary

a={}
b=[]
train_text = state_union.raw("2005-GWBush.txt")
keywords ="multiple inheritance"


question = ""

#gets the keyword and creates a technical question

def gen_Question(keywords,questionno,nesornot):
    global question
    custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
    tokenized = custom_sent_tokenizer.tokenize(keywords)
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            # print(tagged)
            # namedEnt = nltk.ne_chunk(tagged, binary=True)
            # gen_Question(namedEnt)
            # namedEnt.draw()

        key, words = zip(*tagged)
        #print(key)

        compare = list(words)
        print(words)
        print(compare)
        a = dict(zip(key, words))
        b= dict(zip(words, key))

        print(a)
        print("hey")
        # print([b for b, v in a.items() if v in l1])

    except Exception as e:
        print(str(e))



    if compare == TechnicalQuestionDictionary.tl1:
        question = "What is a "+ keywords

    elif compare ==   TechnicalQuestionDictionary.tl2:
        question = "Can you explain "+ keywords

    elif compare ==  TechnicalQuestionDictionary.tl3:
        question = "Describe about "+ keywords

    elif compare ==  TechnicalQuestionDictionary.tl4:
        question = "What is a "+ keywords

    elif compare == TechnicalQuestionDictionary.tl5:
        question = "What are "+ keywords

    elif compare == TechnicalQuestionDictionary.tl6:
        question = "What is a "+ keywords

    elif compare == TechnicalQuestionDictionary.tl7:
        question = "What are "+ keywords

    elif compare == TechnicalQuestionDictionary.tl9:
        question = "What is a "+ keywords

    elif compare ==  TechnicalQuestionDictionary.tl10:
        question = "What are "+ keywords

    elif compare ==  TechnicalQuestionDictionary.tl11:
        question = "What is a "+ keywords

    elif compare ==  TechnicalQuestionDictionary.tl12:
        question = "How to use"+ keywords

    elif compare ==  TechnicalQuestionDictionary.tl13:
        question = "What is a "+ keywords

    elif compare ==  TechnicalQuestionDictionary.tl14:
        question = "Describe about "+ keywords

    elif compare ==  TechnicalQuestionDictionary.tl15:
        question = "Describe about "+ keywords

    elif compare ==  TechnicalQuestionDictionary.tl16:
        question = "Describe about "+ keywords

    elif compare ==  TechnicalQuestionDictionary.tl17:
        question = "Tell about "+ keywords

    elif compare ==  TechnicalQuestionDictionary.tl18:
        question = "Explain about "+ keywords

    elif compare ==  TechnicalQuestionDictionary.tl19:
        question = "Describe "+ keywords

    elif compare ==  TechnicalQuestionDictionary.tl20:
        question = "What is a "+ keywords

    elif compare ==  TechnicalQuestionDictionary.tl21:
        question = "Describe about "+ keywords

    elif compare ==  TechnicalQuestionDictionary.tl22:
        question = "Tell about "+ keywords

    else:
        question = "Define about " + keywords

    print(vik_test_codes.question(question, questionno))
    print(question)

    voice_record = AudioRecorder.audio_recorder(questionno)
    answer_validity = SpeachToText.validation(keywords, "technical", nesornot, "question" + str(questionno))[0]

    # if questionno == "20" or questionno == 20:
    #
    #     filelist = glob.glob("Audio/*.wav")
    #     for file in filelist:
    #         os.remove(file)


    return question
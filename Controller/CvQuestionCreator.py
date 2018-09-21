import time
from xml.etree import ElementTree
from Controller import TextToSpeechConverter,TechnicalQuestions
import random
from Controller import SpeachToText


lang = 'en'
result = None
count = 0
file_name = '../Database/CvQuestions.xml'

dom = ElementTree.parse(file_name)

starting_question = dom.find('Session[@name="Start"]/Question/Q')
session1_questions = dom.findall('Session[@name="One"]/Question/Q')
# answer = input()

while (result != 1 and count<=5):
        # answer = input()
        time.sleep(0)
        starting_question_text = starting_question.text
        if count==0:
            TextToSpeechConverter.text_to_speech(starting_question_text, lang)
            print(starting_question_text)
        answer = SpeachToText.validation(starting_question_text)
        print(answer)
        count = count+1
        if (count==5 or answer==1):
            result = 1
count =0

for c in session1_questions:
    result = None
    while (result != 1 and count<=5):
        # answer = input()
        time.sleep(0)
        if count==0:
            session1_questions_text = c.text
            TextToSpeechConverter.text_to_speech(session1_questions_text, lang)
            print(session1_questions_text)
        session1_questions_text = c.text
        answer = SpeachToText.validation(session1_questions_text)
        print(answer)
        count = count+1
        if (count==5 or answer==1):
            result = 1
    count =0

session2_question = dom.findall('Session[@name="Two"]/Question/Q')

question_list=[]
for q in session2_question:
    question_list.append(q.text)
for pri in range(2):
    result = None
    while (result != 1 and count <= 5):
        # answer = input()
        time.sleep(0)
        random_question = random.choice(question_list)
        if count == 0:
            TextToSpeechConverter.text_to_speech(random_question, lang)
            print(random_question)
            question_list.remove(random_question)

        answer = SpeachToText.validation(random_question)
        print(answer)
        count = count + 1
        if (count == 5 or answer == 1):
            result = 1
    count = 0


session3_questions = dom.findall('Session[@name="Three"]/Question/Q')

for c in session3_questions:
    result = None
    while (result != 1 and count <= 5):
        # answer = input()
        time.sleep(0)
        session3_questions_text = c.text
        if count == 0:
            TextToSpeechConverter.text_to_speech(session3_questions_text, lang)
            print(c.text)
        answer = SpeachToText.validation(session3_questions_text)
        print(answer)
        count = count + 1
        if (count == 5 or answer == 1):
            result = 1
    count = 0



TechnicalQuestions.question_generator()





















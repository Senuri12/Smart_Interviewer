from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from Controller import WeightOfTheAnswer
from Controller import ConnectionToNeo4j
from Controller import vari

def ValidatingTechnical(userAnswer, dbAnswer ,qno):

    sentence1 = userAnswer
    sentence2 = dbAnswer

    grammarMarks = WeightOfTheAnswer.process_content(sentence1)

    if len(sentence1.split()) == 0:

        return ['None', '']

    else:

        stopWords = set(stopwords.words('english'))

        words1 = word_tokenize(sentence1)
        words2 = word_tokenize(sentence2)

        wordsFiltered1 = []
        wordsFiltered2 = []

        newSentence = ""

        for w in words1:
            if w not in stopWords:
                wordsFiltered1.append(w)
                newSentence = newSentence + " " + w


        for w in words2:
            if w not in stopWords:
                wordsFiltered2.append(w)

        marks = 0
        final_word = ""

        for word2 in wordsFiltered2:
            for word1 in wordsFiltered1:
                if word2 == word1:
                    marks+= 1

        for word in wordsFiltered2:
            final_word = final_word+" "+word

        wordcountofdbanswer = len(final_word.split())
        print(marks)
        print(wordcountofdbanswer)
        finalmark = (marks/wordcountofdbanswer)+grammarMarks
        finalmark = "%.2f" % finalmark
        # finalmark = SequenceMatcher(None, wordsFiltered1, wordsFiltered2).ratio()

        ConnectionToNeo4j.sessionMarksStoring(vari.userId, "", qno, finalmark)

        return_Value = [finalmark,newSentence]


        return return_Value

def ValidatingNonTechnical(answer,qno):

    answerwordcount = len(answer.split())

    stopWords = set(stopwords.words('english'))

    words1 = word_tokenize(answer)

    wordsFiltered1 = []

    newSentence = ""

    for w in words1:
        if w not in stopWords:
            wordsFiltered1.append(w)
            newSentence = newSentence + " " + w

    if answerwordcount == 0:
        ConnectionToNeo4j.sessionMarksStoring(vari.userId, "", qno, '0')
        return ['None', '']
    if answerwordcount < 20:
        ConnectionToNeo4j.sessionMarksStoring(vari.userId, "", qno, '0.5')
        return [0.5, newSentence]
    if answerwordcount > 20:
        ConnectionToNeo4j.sessionMarksStoring(vari.userId, "", qno, '1')
        return [1, newSentence]
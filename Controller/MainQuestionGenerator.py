from Controller import TechnicalQuestions,NonTechnicalQuestions

def startsession():
    NonTechnicalQuestions.generate_cv_questions()
    TechnicalQuestions.question_gen()

# startsession()s
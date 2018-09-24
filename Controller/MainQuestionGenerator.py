from Controller import TechnicalQuestions,NonTechnicalQuestions

def startsession():
    #generates the cv questions
    NonTechnicalQuestions.generate_cv_questions()
    #generates the technical questions
    TechnicalQuestions.question_gen()

# startsession()
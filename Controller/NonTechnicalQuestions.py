import random,time
from Controller import ConnectionToNeo4j,QuestionCreator,NestedQuestionCreator,vari,AudioRecorder
from Controller import SpeachToText
from gingerit.gingerit import GingerIt
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)




# technology_list = []



#gnerates non technical questions
def generate_cv_questions():
    userid = vari.userId
    global grammer_corrected_pr0ject_question
    db = "CV"
    db2= "project"
    db3 ="project_d"
    # node_Count = ConnectionToNeo4j.getNodeCount(db)
    lang = 'en'
    q_list = []
    pro_list = []
    count = 1
    session = 0
    typo = "nonested"
    typo2 = "nontechnical"
    answer_validity = 0


    global question_number
    question_number = 0

#generates questions from the three sections
    while count<=3:
        session = session + 1
        print("session")
        print(session)
        session_no_string = str(session)
        session_node_count = ConnectionToNeo4j.session_Node_Count(db,session_no_string)
        print("this is ")
        print(session_node_count)
        node_id = ConnectionToNeo4j.get_node_id(db,session_no_string)

        for id in range(node_id,session_node_count+node_id):
            q_list.append(str(id))
        print(q_list)

        print("node_count")
        print(session_node_count)

        for question_no in range(session_node_count):

            print("question number")
            print(question_no)
            random_que = random.choice(q_list)
            print("random que")
            print(random_que)
            #new pars



            non_technical_question = ConnectionToNeo4j.cvQuestionGen(db,random_que)
            q_list.remove(random_que)
            print(q_list)
            print("jokes"+non_technical_question)

            question_number = question_number + 1

            actual_question = QuestionCreator.gen_Question(non_technical_question,question_number)
            # print(actual_question)
            # parser = GingerIt()
            # grammer_corrected_question_list = parser.parse(actual_question)
            # grammer_corrected_question = grammer_corrected_question_list.get("result")
            # TextToSpeechConverter.text_to_speech(grammer_corrected_question, lang)

            # print(question_number)
            # print("hiiiiiiiiiiiiiiiiii printing count")


            #gets an input to ask questions
            if random_que=="5":
                # voice_record = AudioRecorder.audio_recorder(question_number)
                # answer_validity = SpeachToText.validation("", typo2, typo, "question" + str(question_number))[0]

                pro = ConnectionToNeo4j.getProjects(db, "5")
                # print(pro)
                for id in range (1,pro+1):
                    pro_list.append(str(id))
                # print(pro_list)


                random_proj_que = random.choice(pro_list)
                modify_random_proj_que = "p"+random_proj_que
                # print(modify_random_proj_que)

                project_question = ConnectionToNeo4j.cvQuestionProjectGen(db2,db3,modify_random_proj_que,userid)
                question_number = question_number + 1

                actual_project_question = QuestionCreator.gen_Question(project_question,question_number)
                # print(actual_project_question)
                # parser = GingerIt()
                # grammer_corrected_project_question_list = parser.parse(actual_project_question)
                # grammer_corrected_pr0ject_question = grammer_corrected_project_question_list.get("result")

                # TextToSpeechConverter.text_to_speech(grammer_corrected_pr0ject_question, lang)
                # print(question_number)
                # print("hiiiiiiiiiiiiiiiiii printing count")

                global technology_list
                tech = SpeachToText.validation("", typo2,typo,"question"+str(question_number))[1]

                tech = NestedQuestionCreator.keywordSelector("",tech.lstrip(),"1","")
                tech = "i know everything"
                print(tech)
                print("tech printed")
                technology_list = NestedQuestionCreator.nonTechnicalKeywordSeelector(tech,modify_random_proj_que)
                print("hello tech")
                print(technology_list)
                # print("check validity")
                # answer_validity = input()

            print("after a while")

            # voice_record = AudioRecorder.audio_recorder(question_number)
            # answer_validity = SpeachToText.validation("", typo2,typo,"question"+str(question_number))[0]



            # while(answer_validity=="None" ):
            #     answer_validity = SpeachToText.validation("", typo2,typo,"question"+str(question_number))[0]


        q_list = []
        count = count+1








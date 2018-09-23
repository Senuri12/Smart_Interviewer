from py2neo import Graph

graph = Graph("http://neo4j:Sepalika1993@127.0.0.1:7474/db/data")


def ontologyQuestionGen(id):
  query = "MATCH (j:Java{id:"+ id+"}) RETURN j.topic"
  gen_Question = graph.run(query).evaluate()
  # print(gen_Question)
  return gen_Question

# ontologyQuestionGen("1")


def getValueFromdb(subsection,type):

    if type == 'nested':
        subsection = "" + subsection
        exist = "MATCH(b:subB{Name:'"+subsection+"'})RETURN b.Details"
        validationValue = graph.run(exist).evaluate()
        print(validationValue)
        return validationValue
    else:
        subsection = "" + subsection
        exist = "MATCH(a: language) - [r: has]->(b:sub{Name:'" + subsection + "'})RETURN b.Details"
        validationValue = graph.run(exist).evaluate()
        print(validationValue)
        return validationValue

def cvQuestionGen(db,id):
  query = "MATCH (j:"+db+"{id:"+ id+"}) RETURN j.topic"
  gen_Question = graph.run(query).evaluate()
  # print(gen_Question)
  return gen_Question

def cvQuestionProjectGen(db,db2,pid,user):
  # query = "MATCH (j:"+db+"{pid:'"+ pid+"'}) RETURN j.topic"
  query = "MATCH (j:" + db + "{pid:'" + pid + "'}) - [r: projects_details]->(b:" + db2 + "{uid:'" + user + "'}) RETURN b.topic "
  gen_Question = graph.run(query).evaluate()
  print(gen_Question)
  return gen_Question

# cvQuestionProjectGen("CV","p1","uid001")

def session_Node_Count(db,session):
  # session ="2"
  query = "MATCH (a:"+db+"{session: " +session+ "}) RETURN count(*)"
  gen_count = graph.run(query).evaluate()
  # print(gen_count)
  return  gen_count


def get_node_id(db,session):
  query = "MATCH (a:"+db+"{session: " + session + "}) RETURN a.id"
  gen_count = graph.run(query).evaluate()
  # print(gen_count)
  return gen_count
# get_node_id("CV","2")



def technical_question_keyword(table,id):
  val = "1"


  query = "MATCH(a:language{Name:'"+table+"'}) - [r: has]->(b:sub{id:'"+id+"'})RETURN b.Name"
  gen_Question = graph.run(query).evaluate()
  # print(gen_Question)
  return gen_Question
# table ="java"
# technical_question_keyword(table)

def getTechNodeCount(db):
  query = "MATCH(a:language{Name:'"+db+"'}) - [r: has]->(b:sub{})RETURN count(*)"
  gen_count = graph.run(query).evaluate()
  # print(gen_count)
  print("inside the function")
  return gen_count


def getProjects(db,id):
    query = "MATCH (a:"+db+"{id:"+id+"})-[:projects]->(proj) RETURN count(*)"
    # query = "MATCH (a:CV{id:5})-[:projects]->(projects)RETURN count(*)"

    get_projects =graph.run(query).evaluate()
    return get_projects
    # print(get_projects)

def getMatchingTopics(db,topic):
    query = "MATCH(a:language{Name:'" + db + "'}) - [r: has]->(b:sub{Name:'"+topic+"'}) -[r2:nested_has]->(c:subB) RETURN count(c.Name)>0"
    get_availability = graph.run(query).evaluate()
    print(get_availability)
    return get_availability

def getMatchingNestedTopicId(db,topic):
    query = "MATCH(a:language{Name:'" + db + "'}) - [r: has]->(b:sub{Name:'"+topic+"'}) -[r2:nested_has]->(c:subB) RETURN c.id"
    get_availability = graph.run(query).evaluate()
    print(get_availability)
    return get_availability

def getMatchingNestedTopic(db,topic,nesid):
    query = "MATCH(a:language{Name:'" + db + "'}) - [r: has]->(b:sub{Name:'"+topic+"'}) -[r2:nested_has]->(c:subB{id:'"+nesid+"'}) RETURN c.Name"
    get_availability = graph.run(query).evaluate()
    print(get_availability)
    return get_availability
#getMatchingNestedTopic("java","object oriented programming","NES_003")

def getMatchingTopicsNonTech(db):
    query = "MATCH(a:language{Name:'" + db + "'}) - [r: has]->(b:sub)RETURN count(b)>0"
    availability = graph.run(query).evaluate()
    return availability


def cvProjectTech(db,db2,pid,userId):
  # query = "MATCH (j:"+db+"{pid:'"+ pid+"'}) RETURN j.technologies"
  query = "MATCH (j:" + db + "{pid:'" + pid + "'}) - [r: projects_details]->(b:" + db2 + "{uid:'" + userId + "'}) RETURN b.technologies"
  gen_Question = graph.run(query).evaluate()
  print(gen_Question)
  return gen_Question
# cvProjectTech("project","project_d","p1","uid001")

#returns the difficulty level list
def getdiffLevelList(userId,db,db2,techno,level):
    query = "MATCH (j:" + db + "{uid:'" + userId + "'}) - [r: level]->(b:" + db2 + "{technology:'" + techno + "'}) RETURN b." + level+""
    gen_list = graph.run(query).evaluate()
    print("my generated list")

    print(gen_list)
    print("my generated list")
    return gen_list

def getNestedDiffLevelList(userId,db,db2,db3,techno,level):
    query = "MATCH (j:" + db + "{uid:'" + userId + "'}) - [r: level]->(b:" + db2 + "{technology:'" + techno + "'}) -[r2:nested_level] ->(c:"+db3+") RETURN c." + level+""
    gen_list = graph.run(query).evaluate()
    print(gen_list)
    return gen_list

#getNestedDiffLevelList("uid001","user_difficulty", "difficulty","nested_difficulty","python", "medium")


#generates the session details
def getQuestionMarks(db,db2,userId,sessid,number):
    print(db)
    print(db2)
    print(userId)
    print(sessid)
    print(number)
    query = "MATCH(a: "+db+"{Userid: '" + userId + "'}) - [r: userTOsession]->(b:"+db2+"{no: '"+sessid+"'}) return b."+number+""
    gen_mark = graph.run(query).evaluate()
    print("marks will be printed not to worry")

    print(gen_mark)
    print("marks will be printed not to worry")
    return gen_mark



#getQuestionMarks("user","session","uid001","1","question1")


    # pro = cvProjectTech("CV",'p1')
#
# print(pro)

def sessionMarksStoring(Userid,Session,question,marks):

    newSession = ""

    query = "MATCH(a: user{Userid: '"+Userid+"'}) return a.Userid"
    userExist = graph.run(query).evaluate()

    if (userExist == None):

        query1 = "MATCH(c: root{Name: 'Session'}) CREATE(c) - [x: rootTOuser]-> (a: user{Userid:'"+Userid+"'})"
        graph.run(query1).evaluate()




    if question == "question1":
        query13 = "MATCH (n:session) RETURN n.no ORDER BY n.no DESC LIMIT 1;"
        sessionExist1 = graph.run(query13).evaluate()
        if sessionExist1== None:
            sessionExist1 = 0
        number = int(sessionExist1)+1
        query14 = "MATCH(a: user{Userid: '"+Userid+"'}) CREATE(a) - [r: userTOsession]->(b:session{no: '" + str(number) + "'})"
        graph.run(query14).evaluate()

    # query3 = "MATCH(a: user{Userid: '"+Userid+"'}) - [r: userTOsession]->(b:session{no: '" + Session + "'}) return b.no"
    # sessionExist = graph.run(query3).evaluate()
    #
    # if (sessionExist == None):
    #
    #     query4 = "MATCH(a: user{Userid: '"+Userid+"'}) CREATE(a) - [r: userTOsession]->(b:session{no: '" + Session + "'})"
    #     graph.run(query4).evaluate()

    query3 = "MATCH (n:session) RETURN n.no ORDER BY n.no DESC LIMIT 1;"
    newSession = graph.run(query3).evaluate()


    query5 = "MATCH(a: user{Userid: '" + Userid + "'}) - [r: userTOsession]->(b:session{no: '" + newSession + "',"+question+":'"+marks+"'}) return b.no"
    questionExist = graph.run(query5).evaluate()

    if (questionExist == None):

        query6 = "MATCH(a: user{Userid: '"+Userid+"'}) - [r: userTOsession]->(b:session{no: '" + newSession + "'}) SET b."+question+" = '"+marks+"' RETURN b"
        marking = graph.run(query6).evaluate()

    return questionExist



def createQtable1(languageName):
    exist = "MATCH (n:language) where n.Name='" + languageName + "' return n.qtable"
    qtableValue = graph.run(exist).evaluate()
    return qtableValue


# this is to send and update values
def sendQtable(languageName,qTableCreated):
    query = "Match (n:language) where n.Name='" + languageName + "' SET n.qtable='" + qTableCreated + "'  RETURN n.qtable"
    qtableValue1 = graph.run(query).evaluate()
    return qtableValue1

#send the node list updated existing category-asked 1 remove krarapu 1
def sendExistingDifficultyList(userid,languageName,difficultyLevel,str_getDiffList3):
    exist = "MATCH(n: user_difficulty{uid: '" + userid + "'}) - [r: level]->(b:difficulty{technology: '" + languageName + "'}) SET b." + difficultyLevel + " ='" + str_getDiffList3 + "' return b." + difficultyLevel + ""
    qtableValue = graph.run(exist).evaluate()
    return qtableValue

 #get the difficulty list that wants to update - new list
def getNewRewardList(userid,languageName,rewardState):
    exist = "MATCH(n: user_difficulty{uid: '" + userid + "'}) - [r: level]->(b:difficulty{technology: '" + languageName + "'}) return b."+rewardState+""
    qtableValue = graph.run(exist).evaluate()
    return qtableValue


#get the easy, medium, hard to list
def getDifficultyList(userid,langName,category):
    exist = "MATCH(n: user_difficulty{uid: '" + userid + "'}) - [r: level]->(b:difficulty{technology: '" + langName + "'}) return b." + category + ""
    qtableValue = graph.run(exist).evaluate()
    print("hello anuruddha")
    print(qtableValue)
    return qtableValue

#set the new value to node
def sendNewDifficultyList(userid,languageName,rewardState,str_getDiffList4):
    exist = "MATCH(n: user_difficulty{uid: '" + userid + "'}) - [r: level]->(b:difficulty{technology: '" + languageName + "'}) SET b." + rewardState + " = '" + str_getDiffList4 + "' return b."+rewardState+""
    qtableValue = graph.run(exist).evaluate()
    return qtableValue













from Controller import ConnectionToNeo4j,vari
import random


# db = "python"
#checks whether the topics are available to create a nested question if exist returns a topic
def keywordSelector(db,filtered_words_string,param,diff_level):
    db2 ="user_difficulty"
    db3 = "difficulty"
    db4 = "nested_difficulty"
    user_id = vari.userId
    print("diff_level")
    print(diff_level)
    print("diff_level")

    filtered_words_string = filtered_words_string.replace("'", " ")
    filtered_words = filtered_words_string.split(" ")
    print(filtered_words)
    print("filtered_words")


    global  topic_list
    topic_list = []

    global nested_keyword_list
    nested_keyword_list = []

    global nested_difficulty_list
    nested_difficulty_list = []

    global nes_keywords

    # print(filtered_words)
    unique_filtered_words = set()
    for val in filtered_words:
        lower_case_val = val.lower()
        unique_filtered_words.add(lower_case_val)
    # added
    # unique_filtered_words.add("tupple")
    print(unique_filtered_words)
    print("unique_filtered_words")

    for value in unique_filtered_words:
        if param == "2":
            print(db)
            print(value)
            topic_availability = ConnectionToNeo4j.getMatchingTopics(db,value)
            print(topic_availability)
            if topic_availability == True:
                topic_list.append(value)
        elif param == "1":
            topic_availability = ConnectionToNeo4j.getMatchingTopicsNonTech(value)
            print(topic_availability)
            if topic_availability == True:
                topic_list.append(value)
    print(topic_list)
    print("topic_list")
    # print(topic_list)
    if param == "1":
        topic_list = ",".join(topic_list)
        return topic_list


    if len(topic_list) > 0 and param=="2":
        for itt in range (len(topic_list)):
            random_keyword = random.choice(topic_list)
            nes_keywords=ConnectionToNeo4j.getMatchingNestedTopicId(db,random_keyword)
            print(random_keyword)
            print("random_keyword")
            nested_keyword_list = (nes_keywords.split(',' ))
            print(nested_keyword_list)
            print(nested_keyword_list)
            print("random_keyword")

            nes_diff_level = ConnectionToNeo4j.getNestedDiffLevelList(user_id,db2,db3,db4,db,diff_level)
            print("nes_diff_level")
            print(nes_diff_level)
            print("nes_diff_level")

            nested_difficulty_list = (nes_diff_level.split(',' ))


            print("nested_difficulty_list")
            print(nested_difficulty_list)
            print("nested_difficulty_list")

            selected_list = set(nested_difficulty_list) & set(nested_keyword_list)
            print("selected_list")
            print(selected_list)
            print("selected_list")
            selected_list = list(selected_list)



            print("selected_list")
            print(selected_list)
            print("selected_list")
            if not selected_list:
                return 0

            random_nes_que = random.choice(selected_list)
            print("random_nes_que")
            print(random_nes_que)
            print("random_nes_que")

            topic = ConnectionToNeo4j.getMatchingNestedTopic(db,random_keyword,random_nes_que)
            print("topic")
            print(topic)
            print("topic")

            return topic

    else:
        return 0

# keyword = keywordSelector();
# for()

#gets the technical keyword list and if no topic available access the db and gets the values
def nonTechnicalKeywordSeelector(names,project):
    user_id = vari.userId

    name_list = names.split(' ')
    print("name list")
    print(name_list)
    db_list = []

    unique_filtered_word_nontech = set()
    for val in name_list:
        lower_case_value = val.lower()
        unique_filtered_word_nontech.add(lower_case_value)
        print(unique_filtered_word_nontech)
        print("error in yesterday")
    for value in unique_filtered_word_nontech:
        db_availability = ConnectionToNeo4j.getMatchingTopicsNonTech(value)
        print("error in now")
        if db_availability == True:
            db_list.append(value)
        print(db_list)
        print("it is printed")
    if len(db_list) > 0:
        db_string_list = ','.join(db_list)
        print(db_string_list)
        print("error in that")
        return  db_string_list
    else:
        db = "project"
        db2 = "project_d"
        project_tech_list = ConnectionToNeo4j.cvProjectTech(db,db2,project,user_id)
        print("error in this")
        return project_tech_list


# listings =nonTechnicalKeywordSeelector("i know everything","p1")
# print(listings)





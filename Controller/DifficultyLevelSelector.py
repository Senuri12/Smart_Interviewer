from Controller import ConnectionToNeo4j,vari
#this reduces the difficulty level
def decrease_difficulty_level(level):
    if level == "easy" :
        diff_level = "easy"
    elif level == "medium" :
        diff_level = "easy"
    elif level == "hard" :
        diff_level = "medium"
    return diff_level

#this increases the difficulty level
def increase_difficulty_level(level):
    if level == "easy" :
        diff_level = "medium"
    elif level == "medium" :
        diff_level = "hard"
    elif level == "hard" :
        diff_level = "hard"
    return diff_level


#gets the difficulty level list
def adding_diff_level_val_list(userId,user_diff,db_diff,random_table,diff_level):
    print(userId )
    print(user_diff )
    print( db_diff)
    print(random_table )
    print( diff_level)
    level_list = ConnectionToNeo4j.getdiffLevelList(userId,user_diff,db_diff,random_table,diff_level)
    print(level_list)
    level_list_str = str(level_list)
    print(level_list_str)
    if not level_list_str:
        diff_list = []
        return diff_list
    print("hello i got the list")
    print(level_list)

    diff_list = level_list.split(',')

    print("hello in the diff level selector")
    diff_list = list(map(int, diff_list))
    print(diff_list)
    return (diff_list)

def change_difficulty_level(nodeId,langName):
    userId = vari.userId
    category1 = "easy"
    category2 = "medium"
    category3 = "hard"
    global diffi_new_level

    #checking whether it contains node the easy level
    diffList = ConnectionToNeo4j.getDifficultyList(userId, langName, category1)
    diffList = diffList.split(',')
    for val1 in diffList:
        if val1 ==  nodeId:
            diffi_new_level = "easy"
            return diffi_new_level

    #checking whether it contains node the medium level
    diffList2 = ConnectionToNeo4j.getDifficultyList(userId, langName, category2)
    diffList2 = diffList2.split(',')
    for val2 in diffList2:
        if val2 ==  nodeId:
            diffi_new_level = "medium"
            return diffi_new_level

    #checking whether it contains node the hard level
    diffList3 = ConnectionToNeo4j.getDifficultyList(userId, langName, category3)
    diffList3 = diffList3.split(',')
    for val3 in diffList3:
        if val3 ==  nodeId:
            diffi_new_level = "hard"
            return diffi_new_level
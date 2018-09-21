from Controller import ConnectionToNeo4j
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
    level_list = ConnectionToNeo4j.getdiffLevelList(userId,user_diff,db_diff,random_table,diff_level)
    level_list_str = str(level_list)
    print("hello i got the list")
    print(level_list)

    diff_list = level_list.split(',')
    print("hello in the diff level selector")
    diff_list = list(map(int, diff_list))
    print(diff_list)
    return (diff_list)



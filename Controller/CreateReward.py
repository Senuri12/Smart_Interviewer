# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 21:54:23 2018

@author: ASUS
"""

import numpy as np
from xml.etree import ElementTree as ET
from BackEnd.Controller import ConnectionToNeo4j,rewardVariable


# ---------------------------------------------------------------------------------------------
# Identify the state

facial = int(input("Facial :"))
voice = int(input("Voice :"))
answer = int(input("Answer :"))

total = (facial + voice + answer)

print("Total = ", total)
total = int(total)

if (0 < total <= 20):
    state = 1
    print("State = ", state)

elif (21 < total <= 40):
    state = 2
    print("State = ", state)

elif (41 < total <= 60):
    state = 3
    print("State = ", state)

elif (61 < total <= 80):
    state = 4
    print("State = ", state)

else:
    state = 5
    print("State = ", state)

# -----------------------------------------------------------------------------------
# Get the latest updated q-table from ontology - only for shown
langName = rewardVariable.getLanguageName()
print("@@@@@This part for get from ontology@@@@@@@@@@@@@@@@@@@@@@@@@")
print("It is updated correctly \n", ConnectionToNeo4j.createQtable1(langName))
print(type(ConnectionToNeo4j.createQtable1(langName)))
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

#data = R
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")



#Get the String array matrix from ontology - split
I = np.array(ConnectionToNeo4j.createQtable1(langName)).tolist()
Z = I.split(" ")
print("Z-spit krapu 1 \n",Z)
print(type(Z))


#to remove the []
number = " ".join(Z)
print("this remove[] \n", number)
print(type(number))

print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")


#H = [float(i) if '.' in i else int(i) for i in number]
#H = np.asfarray(number,float)
#print("This str - float")
#print(type(H))
#Re-change it into 5,5 array
#qTableCreated = H.reshape(5,5)
#print(type(qTableCreated))
#print(qTableCreated)

#change it into matrix
# R = np.matrix(number)
# print(type(R))
# print(R)

R = np.matrix([[64.0, 64.0, 64.0, 64.0, 64.0],
               [64.0, 64.0, 64.0, 64.0, 64.0],
               [64.0, 64.0, 64.0, 64.0, 64.0],
               [64.0, 64.0, 64.0, 64.0, 64.0],
               [64.0, 64.0, 64.0, 64.0, 64.0]])
# try:
#     I = float(ConnectionToNeo4j.createQtable1(langName))
#     R = np.matrix(I)
# except ValueError:
#     print("That is not a valid number of miles")

# matrix = open(fname).read()
# matrix = [item.split('\n') for item in matrix.split('\n')]
# R = matrix.reshape((matrix.shape[0], 5))


# print("Get from text file-latest updated \n", R)

print("----------------------------------------------")
# Q matrix
Q = np.matrix(np.zeros([5, 5]))

if state == 1:
    R[0, 4] = total
elif state == 2:
    R[1, 3] = total
elif state == 3:
    R[2, 2] = total
elif state == 4:
    R[3, 1] = total
else:
    R[4, 0] = total

# Gamma (learning parameter).
gamma = 0.8

# Initial state
if state == 5:
    initial_state = 4
else:
    initial_state = state


# initial_state = state
# This function returns all available actions in the state given as an argument
def available_actions(state):
    current_state_row = R[state,]
    av_act = np.where(current_state_row >= 0)[1]
    return av_act


# Get available actions in the current state
available_act = available_actions(initial_state)


# This function chooses at random which action to be performed within the range
def sample_next_action(available_actions_range):
    next_action = int(np.random.choice(available_act, 1))
    return next_action


# Sample next action to be performed
action = sample_next_action(available_act)


# This function updates the Q matrix
def update(current_state, action, gamma):
    max_index = np.where(Q[action,] == np.max(Q[action,]))[1]

    if max_index.shape[0] > 1:
        max_index = int(np.random.choice(max_index, size=1))
    else:
        max_index = int(max_index)
    max_value = Q[action, max_index]

    # Q learning formula
    Q[current_state, action] = R[current_state, action] + gamma * max_value


# Update Q matrix
update(initial_state, action, gamma)

# -------------------------------------------------------------------------------
# Create the reward value

# iterarte the process
for i in range(100):
    current_state = np.random.randint(0, int(Q.shape[0]))
    available_act = available_actions(current_state)
    action = sample_next_action(available_act)
    update(current_state, action, gamma)
print("-----------------------")
print("New updated one \n", Q)
print("-----------------------")
# ----------------------------------------------------------------------------------------------------------------
# Save the Q-metrix in text file

print(" Maximum value:")
print(np.max(Q))
T = Q * 100 / np.max(Q)
print("^^^^^^^^^^^^^^^^^^^^^^^^^^")
print(T)
np.savetxt('../Database/text.txt', T, fmt='%f')

print("-----New - 6-----------------------------------------")
#-------------------------------------------------------
# send to ontology

qTableCreated = str(T)

ConnectionToNeo4j.sendQtable(langName,qTableCreated)
# -------------------------------------------------------------------------------
print("------New - 7----------------------------------------")
# convert to probability value

if state == 3:
    convertProb = "{0:.0f}%".format((np.max(Q) / 10) - 11)
    # convertProb = getProb - 10.0
    print("Precentage of difficulty - ", convertProb)
else:
    convertProb = "{0:.0f}%".format(np.max(Q) / 10)
    print("Precentage of difficulty - ", convertProb)

#--send to precentage value to ontology--------------
print(type(convertProb))

convertProb2 = int(convertProb.strip("%"))
print(convertProb2)


#--identify the state--------------
print("------New - 8----------------------------------------")
if convertProb2 <= 15:
    rewardState = "hard"
elif convertProb2 <= 30:
    rewardState = "medium"
else:
    rewardState = "easy"

print(rewardState)

#--update the ontology---------------------------
print("-------New - 9---------------------------------------")
userid = rewardVariable.userid
nodeid = rewardVariable.getNodeID()
category = rewardVariable.getCategoryName()

print(ConnectionToNeo4j.getDifficultyList(userid, langName, category))

getDiffList = str(ConnectionToNeo4j.getDifficultyList(userid, langName, category))
print("get existing list",getDiffList)


getDiffList2 = getDiffList.split(',')
getDiffList2.remove(nodeid)
getDiffList3 = list(map(int, getDiffList2))
print(type(getDiffList3))
str_getDiffList3 = ','.join(str(e) for e in getDiffList3)
print("This is converted str", str_getDiffList3)
print(type(str_getDiffList3))

def sendNewDiffList(userid, langName, rewardState, str_getDiffList3):
    #getDiffList4 = str(getDiffList3)
    ConnectionToNeo4j.sendNewDifficultyList(userid, langName, rewardState, str_getDiffList3)
    print("this is in the function\n",str_getDiffList3)


sendNewDiffList(userid, langName, rewardState, str_getDiffList3)




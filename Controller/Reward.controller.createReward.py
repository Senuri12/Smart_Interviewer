# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 21:54:23 2018

@author: ASUS
"""


import numpy as np
from xml.etree import ElementTree as ET
#import matlab-python as matlab


#---------------------------------------------------------------------------------------------
#Identify the state

facial = int(input("Facial :"))
voice = int(input("Voice :"))
answer = int(input("Answer :"))

total = (facial + voice + answer)
#total = 54;
print("Total = ",total)
total = int(total)

if (0 < total <= 20):
    state = 1
    print ("State = ",state)

elif (21 < total <= 40):
    state = 2
    print ("State = ",state)

elif (41 < total <= 60):
    state = 3
    print ("State = ",state)

elif (61 < total <= 80):
    state = 4
    print ("State = ",state)

else:
    state = 5
    print ("State = ",state)



#----------------------------------------------------------------------------------------------------------------
#Create the metrix

R = np.matrix([[0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0]])

# -------------------------------------------------------------------------------
# Get the latest Q-table reguarding the language

fname = "../Database/text.txt"

with open(fname, 'r') as f:
    data = np.genfromtxt(f,dtype="float")

data = R

print("----------------------------------------------")
# Q matrix
Q = np.matrix(np.zeros([5, 5]))

if state == 1:
    R[0,4] = total
elif state == 2:
    R[1,3] = total
elif state == 3:
    R[2,2] = total
elif state == 4:
    R[3,1] = total
else:
    R[4,0] = total


# Gamma (learning parameter).
gamma = 0.8

# Initial state
initial_state = 1


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
for i in range(10000):
    current_state = np.random.randint(0, int(Q.shape[0]))
    available_act = available_actions(current_state)
    action = sample_next_action(available_act)
    update(current_state, action, gamma)

#----------------------------------------------------------------------------------------------------------------
#Save the Q-metrix in text file

print(" Maximum value:")
print(np.max(Q))
T = Q * 100 / np.max(Q)
np.savetxt('../Database/text.txt', T, fmt='%f')


# -------------------------------------------------------------------------------
# convert to probability value

if state == 3:
    convertProb = "{0:.0f}%".format((np.max(Q) / 10)-11)
    # convertProb = getProb - 10.0
    print("Precentage of difficulty - ",convertProb)
else:
    convertProb = "{0:.0f}%".format(np.max(Q) / 10)
    print("Precentage of difficulty - ",convertProb)



# -------------------------------------------------------------------------------
# update the XML file

tree = ET.parse('../Database/rewardValue.xml')
root = tree.getroot()

# modifying an attribute Language
for elem in root.iter('language'):
    elem .set('name', 'java')

# modifying an attribute Session
for elem in root.iter('session'):
    elem.set('name', '1')

# changing a field text
for elem in root.iter('session'):
    elem.text = convertProb

tree.write('../Database/rewardValue.xml')


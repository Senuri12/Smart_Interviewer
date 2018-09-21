import time
import os
import glob



def question(a,b):
    print(a)


    if isinstance(a, str):

        question = a

        open('Controller/questionSaver_testing.py', 'w').close()
        fruits = ["global gcpq\n", "gcpq = '" + question + "'\n"]
        new_file = open("Controller/questionSaver_testing.py", mode="a+", encoding="utf-8")
        new_file.writelines(fruits)
        for line in new_file:
            print(line)

        new_file.close()

        if b == "20" or b == 20:
            time.sleep(20)
            print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhjjjjjjjjjjj")
            open('Controller/questionSaver_testing.py', 'w').close()
            fruits = ["global gcpq\n", "gcpq = 'end'\n"]
            new_file = open("Controller/questionSaver_testing.py", mode="a+", encoding="utf-8")
            new_file.writelines(fruits)
            for line in new_file:
                print(line)

            new_file.close()

            filelist = glob.glob("Audio/answer_creation_purposes/*.wav")
            for file in filelist:
                os.remove(file)




    return a
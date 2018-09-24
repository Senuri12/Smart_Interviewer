from flask import Flask, render_template,request
import json
from Controller import vari

import userDetails
from Controller import TechnicalQuestions,NonTechnicalQuestions,MainQuestionGenerator,questionSaver_testing,ConnectionToNeo4j
#test eka wenuwata sarindige py file name eka danna haha1 method eka athuleth change karanna
import test
# import userDetails,jaha
from threading import Thread



app = Flask(__name__)



global result12
result12 = 'ram'


@app.route('/')
def hello_world():
    open('userDetails.py', 'w').close()
    fruits = ["global results12\n", "results12 = 'no'"]
    new_file = open("userDetails.py", mode="a+", encoding="utf-8")
    new_file.writelines(fruits)
    for line in new_file:
        print(line)

    new_file.close()

    return render_template('index.html')

@app.route('/interview')
def profile():
    return render_template('bot.html')


@app.route('/dum')
def haha1():

    # async_slow_function()
    result = {"ques": questionSaver_testing.gcpq}
    return json.dumps(result)


#
# def slow_function():
#
#     jaha.go()
#
# def async_slow_function():
#     thr = Thread(target=slow_function)
#     thr.start()
#     return thr


@app.route('/logindata', methods = ['POST'])
def get_post_javascript_data():
    un = request.form['username']
    pw = request.form['password']


    dbpw = ConnectionToNeo4j.login(un)


    print(un)
    if pw == dbpw:
        open('userDetails.py', 'w').close()
        fruits = ["global results12\n", "results12 = 'yes'"]
        new_file = open("userDetails.py", mode="a+", encoding="utf-8")
        new_file.writelines(fruits)
        for line in new_file:
            print(line)

        new_file.close()

    else:
        open('userDetails.py', 'w').close()
        fruits = ["global results12\n", "results12 = 'no'"]
        new_file = open("userDetails.py", mode="a+", encoding="utf-8")
        new_file.writelines(fruits)
        for line in new_file:
            print(line)

        new_file.close()






@app.route('/getloginresult')
def haha2():

    result = {"joking": userDetails.results12}
    return json.dumps(result)

@app.route('/home')
def login():
    return render_template('home.html')


@app.route('/signup')
def register():
    return render_template('signup.html')



# @app.route('/dum1')
# def haha1():
#
#     result = {"ques": test.question1}
#     return json.dumps(result)
#
# @app.route('/dum2')
# def haha2():
#
#     result = {"ques": test.question2}
#     return json.dumps(result)
# @app.route('/dum3')
# def haha3():
#
#     result = {"ques": test.question3}
#     return json.dumps(result)
#
# @app.route('/dum4')
# def haha4():
#
#     result = {"ques": test.question4}
#     return json.dumps(result)
#
#
@app.route('/history')
def history():
    return render_template('history.html')


@app.route('/cv')
def cv():
    return render_template('cvform.html')
# @app.route('/dum5')
# def haha5():
#
#     result = {"ques": test.question5}
#     return json.dumps(result)
#
#
# @app.route('/dum6')
# def haha6():
#
#     result = {"ques": test.question6}
#     return json.dumps(result)
#
#
# @app.route('/dum7')
# def haha7():
#
#     result = {"ques": test.question7}
#     return json.dumps(result)
#
#
# @app.route('/dum8')
# def haha8():
#
#     result = {"ques": test.question8}
#     return json.dumps(result)
#
# @app.route('/dum9')
# def haha9():
#
#     result = {"ques": test.question9}
#     return json.dumps(result)
#
#
# @app.route('/dum10')
# def haha10():
#
#     result = {"ques": test.question10}
#     return json.dumps(result)
#
#
# @app.route('/dum11')
# def haha11():
#
#     result = {"ques": test.question11}
#     return json.dumps(result)
#
#
# @app.route('/dum12')
# def haha12():
#
#     result = {"ques": test.question12}
#     return json.dumps(result)
#
#
# @app.route('/dum13')
# def haha13():
#
#     result = {"ques": test.question13}
#     return json.dumps(result)
#
#
# @app.route('/dum14')
# def haha14():
#
#     result = {"ques": test.question14}
#     return json.dumps(result)
#
#
# @app.route('/dum15')
# def haha15():
#
#     result = {"ques": test.question15}
#     return json.dumps(result)
#
#
# @app.route('/dum16')
# def haha16():
#
#     result = {"ques": test.question16}
#     return json.dumps(result)
#
#
# @app.route('/dum17')
# def haha17():
#
#     result = {"ques": test.question17}
#     return json.dumps(result)
#
#
# @app.route('/dum18')
# def haha18():
#
#     result = {"ques": test.question18}
#     return json.dumps(result)
#
#
# @app.route('/dum19')
# def haha19():
#
#     result = {"ques": test.question19}
#     return json.dumps(result)
#
#
# @app.route('/dum20')
# def haha20():
#
#     result = {"ques": test.question20}
#     return json.dumps(result)


@app.route('/registerdata', methods = ['POST'])
def get_post_javascript_data1():
    print("lalala")
    un = str(request.form['username'])
    pw = str(request.form['password'])
    email = str(request.form['email'])


    jb = ConnectionToNeo4j.register(un,pw,email)

@app.route('/cvdata', methods = ['POST'])
def get_post_cv_javascript_data():
    print("hello ")

    fname = str(request.form['flname'])
    usage = str(request.form['uage'])
    usschool = str(request.form['uschool'])
    usuni = str(request.form['uuni'])
    usdob = str(request.form['udob'])
    usemail = str(request.form['uemail'])
    ustpno = str(request.form['utpno'])
    usweak = str(request.form['uweak'])
    usstrengh = str(request.form['ustrength'])
    usidlcmp = str(request.form['uidcomp'])
    usftech = str(request.form['ufmtech'])
    usproone = str(request.form['uproone'])
    ustech1 = str(request.form['utech1'])
    usprotwo = str(request.form['uprotwo'])
    ustech2 = str(request.form['utech2'])


    uid = vari.userId
    fresult = ConnectionToNeo4j.createNewCv(uid,fname,usage,usschool,usuni,usdob,usemail,ustpno,usweak,usstrengh,usidlcmp,usftech,usproone,ustech1,usprotwo,ustech2)
    print(fname)






if __name__ == '__main__':
    app.run()

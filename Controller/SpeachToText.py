import speech_recognition as sr
from Controller import ConnectionToNeo4j, MostRecentAudioFileAccess, AnswerValidating,AudioRecorder
import os
import glob

def validation(subsection, typer, treetype,qno):

 r = sr.Recognizer()
 audio = "Audio/"+MostRecentAudioFileAccess.MostRecentAudioClip()
 cmd = 'ffmpeg -i ' + audio + ' -f segment -segment_time 13 -c copy Audio/answer_creation_purposes/out%03d.wav'
 os.system(cmd)
 marks = "No"

 longstext = ""

 path, dirs, files = next(os.walk("Audio/answer_creation_purposes"))
 file_count = len(files)
 range_value = file_count
 print('Loading..')
 for x in range(0, range_value):
     audio = 'Audio/answer_creation_purposes/out00' + str(x) + '.wav'

     with sr.AudioFile(str(audio)) as source:
         audio = r.record(source)

     try:
         text = r.recognize_google(audio)
         if x == 0:
             longstext = text
         else:
             longstext = longstext + " " + text

     except Exception as e:
         print(e)

 filelist = glob.glob("Audio/answer_creation_purposes/*.wav")
 for file in filelist:
  os.remove(file)

 print(longstext)

 if typer == "technical":
    valuefromdb = ConnectionToNeo4j.getValueFromdb(subsection, treetype)
    marks = AnswerValidating.ValidatingTechnical(longstext, valuefromdb,qno)
 if typer == "nontechnical":
    marks = AnswerValidating.ValidatingNonTechnical(longstext,qno)


 return marks

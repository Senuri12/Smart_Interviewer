from Controller import MainQuestionGenerator,AudioRecorder
MainQuestionGenerator.startsession()
# print(AudioRecorder.audio_recorder('1'))










from Controller import SpeachToText


q="java  overriding object  technical"

# subsection = input("enter sub area : \n")
# typer = input("enter type : \n")pickling
value = []
value = SpeachToText.validation("mocking", "nontechnical","nonested","question2")
print(value[1])

#
# import os

# max_mtime = 0
# number = "0"
#
# for dirname, subdirs, files in os.walk("Audio/."):
#             for fname in files:
#                 full_path = os.path.join(dirname, fname)
#                 mtime = os.stat(full_path).st_mtime
#                 if mtime > max_mtime:
#                     max_mtime = mtime
#                     max_dir = dirname
#                     max_file = fname
# if max_file[7]==".":
#     number = str(int(max_file[6])+1)
# else:
#     number = max_file[6]+ max_file[7]
#     number = str(int(number)+1)
#
# print("output"+number+".wav")


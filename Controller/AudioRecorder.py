import pyaudio
import wave
import re
import glob
import os
import shutil

def Foldercheck():
    listdirectory = os.listdir("Audio.")
    val = False
    for filename in listdirectory:
        if filename.endswith(".wav"):
            val = True
    return val





def audio_recorder(questionNo):
    max_file = ""
    CHUNK = 1024
    FORMAT = pyaudio.paInt16 #paInt8
    CHANNELS = 2
    RATE = 44100 #sample rate
    RECORD_SECONDS = 20
    if not os.path.exists("/Audio"):
        os.makedirs("Audio")
        print("Created 'Audio' directory")
    jj = Foldercheck()
    if not jj  :

        print("empty directory")
        CURRENT_FILE_NAME = "output0"+ ".wav"
    else:
        max_mtime = 0
        number = "0"
        global mf
        mf=""
        for dirname, subdirs, files in os.walk("Audio/."):
            for fname in files:
                full_path = os.path.join(dirname, fname)
                mtime = os.stat(full_path).st_mtime
                if mtime > max_mtime:
                    max_mtime = mtime
                    max_dir = dirname
                    mf = fname
        if mf[7] == ".":
            number = str(int(mf[6]) + 1)
        else:
            number = mf[6] + mf[7]
            number = str(int(number) + 1)









        CURRENT_FILE_NAME = "output" + number + ".wav"
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK) #buffer
    print("* recording")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data) # 2 bytes(16 bits) per channel
    print("* done recording")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(CURRENT_FILE_NAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    shutil.move(CURRENT_FILE_NAME,"Audio")
    print("Moved "+CURRENT_FILE_NAME+" to Audio directory.")
    return "yes"

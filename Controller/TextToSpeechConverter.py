import time
from gtts import gTTS
import pyglet


def text_to_speech(text,lang):
    audio_file = gTTS(text = text, lang =lang)
    # audio_location = 'BackEnd/tmp/question.mp3'
    audio_location = '../tmp/question.mp3'

    audio_file.save(audio_location)

    play_audio = pyglet.media.load(audio_location)
    play_audio.play()

    time.sleep(play_audio.duration)
    # os.remove(audio_location)
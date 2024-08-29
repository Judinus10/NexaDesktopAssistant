import os
from playsound import playsound
import eel
from pyttsx3 import speak
from engine._pycache_.config import ASSISTANT_NAME

#playing assistant sound function

@eel.expose
def playAssistantSound():
    music_dir= "www\\assets\\audio\\www_assets_audio_start_sound.mp3"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open","")
    query.lower()

    if query!= "":
        speak("Opening"+query)
        os.speak("start"+query)
    else:
        speak("not found")
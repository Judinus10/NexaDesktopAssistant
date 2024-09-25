import os
import re
from playsound import playsound
import eel
from pyttsx3 import speak
from engine._pycache_.config import ASSISTANT_NAME
import pywhatkit as kit

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
        os.system("start"+query)
       
    else:
        speak("not found")
        
def PlayYoutube(query):
    # Assuming `query` is something like "play song on YouTube"
    search_term = query.replace("play ", "").replace("on youtube", "").strip()
    
    # Check if `search_term` is empty or None
    if not search_term:
        speak("I didn't catch what you say, please say it again.")
        return

    speak("Playing " + search_term + " on YouTube")
    
    # Construct the search URL and open YouTube
    url = f"https://www.youtube.com/results?search_query={search_term}"
    os.system(f"start {url}")


def extract_yt_term(command):
    #define regular expression pattern to capture the song name
    pattern=r'play\s+(.*?)\s+on\s+youtube'
    #use re.search to find the match in the command
    match = re.search(pattern,command,re.IGNORECASE)
    #if a match is found, returnde the extract song name, otherwise return none  
    return match.group(1) if match else None
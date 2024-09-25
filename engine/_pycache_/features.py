import os
import re
import sqlite3
from playsound import playsound
import eel
from pyttsx3 import speak
from engine._pycache_.config import ASSISTANT_NAME
import pywhatkit as kit
import webbrowser
from engine._pycache_.db import cursor

#playing assistant sound function

@eel.expose
def playAssistantSound():
    music_dir= "www\\assets\\audio\\www_assets_audio_start_sound.mp3"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "").replace("open", "").strip().lower()

    if query:
        app_name = query.strip()
        try:
            print(f"Debug: Looking for application '{app_name}' in the database.")  # Debugging line
            
            # Fetching application path
            cursor.execute('SELECT path FROM sys_command WHERE name = ?', (app_name,))
            results = cursor.fetchall()
            
            print(f"Debug: Fetched results: {results}")  # Debugging line
            
            if results:
                app_path = results[0][0]  # Access the first element of the tuple
                speak("Opening " + app_name)  # Speak the app name
                os.startfile(app_path)  # Open the application
            else:
                print(f"Debug: No application found. Checking web commands for '{app_name}'.")  # Debugging line
                
                cursor.execute('SELECT url FROM web_command WHERE name = ?', (app_name,))
                results = cursor.fetchall()

                print(f"Debug: Fetched web results: {results}")  # Debugging line
                
                if results:
                    url = results[0][0]  # Access the first element of the tuple
                    speak("Opening " + app_name)  # Speak the app name
                    webbrowser.open(url)  # Open the URL in the web browser
                else:
                    speak("Application or URL not found for " + app_name)
                    print(f"Debug: No application or URL found for '{app_name}'.")  # Debugging line
        except sqlite3.Error as e:
            speak("Database error occurred: " + str(e))
            print(f"Database error: {str(e)}")  # Print detailed database error
        except Exception as e:
            speak("Something went wrong: " + str(e))
            print(f"General error: {str(e)}")  # Print general error message
    else:
        speak("Please specify what you want to open.")
        print("Debug: No query provided to openCommand.")  # Debugging line


    # if query!= "":
    #     speak("Opening"+query)
    #     os.system("start"+query)
       
    # else:
    #     speak("not found")
        
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
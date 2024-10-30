import os
import re
import sqlite3
from pipes import quote
from playsound import playsound
import eel
from engine._pycache_.helper import remove_words
from pyttsx3 import speak
from engine._pycache_.config import ASSISTANT_NAME
import pywhatkit as kit
import webbrowser
from engine._pycache_.db import cursor
# import pvporcupine 
import pyaudio
import struct
import time
import pyautogui
import subprocess
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


# def hotword():
#     porcupine=None
#     paud=None
#     audio_stream=None
#     try:
       
#         # pre trained keywords    
#         porcupine=pvporcupine.create(keywords=["jarvis","alexa"]) 
#         paud=pyaudio.PyAudio()
#         audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
#         # loop for streaming
#         while True:
#             keyword=audio_stream.read(porcupine.frame_length)
#             keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

#             # processing keyword comes from mic 
#             keyword_index=porcupine.process(keyword)

#             # checking first keyword detetcted for not
#             if keyword_index>=0:
#                 print("hotword detected")

#                 # pressing shorcut key win+j
#                 import pyautogui as autogui
#                 autogui.keyDown("win")
#                 autogui.press("b")
#                 time.sleep(2)
#                 autogui.keyUp("win")
                
#     except:
#         if porcupine is not None:
#             porcupine.delete()
#         if audio_stream is not None:
#             audio_stream.close()
#         if paud is not None:
#             paud.terminate()

# Find Contacts
def findContact(query):
    
    
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])
        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('not exist in contacts')
        return 0, 0


def whatsApp(mobile_no, message, flag, name):

    if flag == 'message':
        target_tab = 12
        jarvis_message = "message send successfully to "+name

    elif flag == 'call':
        target_tab = 7
        message = ''
        jarvis_message = "calling to "+name

    else:
        target_tab = 6
        message = ''
        jarvis_message = "staring video call with "+name

    # Encode the message for URL
    encoded_message = quote(message)

    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)
    
    pyautogui.hotkey('ctrl', 'f')

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    speak(jarvis_message)
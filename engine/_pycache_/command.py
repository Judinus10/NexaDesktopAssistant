import pyttsx3
import speech_recognition as sr
import pyaudio
import eel


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate',174)
    engine.say(text)
    engine.runAndWait()

@eel.expose
def takecommand():
    
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listning....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source,10,6)

    try:
        print("recognizing")
        query = r.recognize_google(audio,language ='en-in')
        print(f"user said : (query)")
    except Exception as e:
        return " "
    return query.lower()

text =takecommand()

speak(text)

speak("I'm Jarvis")
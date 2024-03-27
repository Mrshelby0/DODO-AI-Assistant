import pywhatkit
import wikipedia 
from pywikihow import RandomHowTo, search_wikihow
import os 
import speech_recognition as sr
import webbrowser as web
import bs4
import pyttsx3
from time import sleep
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def Speak(audio):
    print("")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print("")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone()as sources:
        print(":Listening............")
        r.pause_threshold =1
        audio = r.listion(sources)

    try:
        print(":Recognizing.........")
        query = r.recognize_google(audio,language='en-in')
        print(f" : your command:{query}\n")
    
    except:
        return ""
    return query.lower()
def YouTubeSearch(term):
    result = "https://www.youtube.com/results?search_query="+term
    web.open(result)
    Speak("This is what i found for your search")
    pywhatkit.playonyt(term)
    Speak("this may also help you")
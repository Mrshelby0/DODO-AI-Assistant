import pyttsx3 #pip install pyttsx3
import time
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import youtube
import smtplib
import random
import pywikihow
import pywhatkit
import os
import sys
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
hour = int(datetime.datetime.now().hour)
engine.setProperty('voice', voices[0].id)
GREETINGS_RES= ["always there for you ","i am ready", "your wish is my command, let's go","how can i help you","i am online and ready to go"]

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
   
    if hour>=0 and hour<12:
        speak("Good Morning! Mr.Shelby")

    elif hour>=12 and hour<18:
        speak("Good Afternoon! Mr.Shelby")   

    else:
        speak("Good Evening! Mr.Shelby")  

    speak("I am Jarvis Mr.Shelby. Please tell me how may I help you")       

def takecommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takecommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif'good morning'in query:
          if hour>=0 and hour<12:
            speak("thank you Mr.Shelby")
            print("thank you Mr.Shelby")
            speak("have a nice day Mr.Shelby")
            print("have a nice day Mr.Shelby")
          else:
            speak("it's not morning Mr.Shelby")
            print("it's not morning Mr.Shelby")
            speak(f"Mr.Shelby the time is {strTime}")
            print(f"Mr.Shelby the time is {strTime}")
            speak("according to the time")
            print("according to the time")
            if hour>=12 and hour<18:
             speak(f"it's  AfterNoon! Mr.Shelby")
             print(f"it's  AfterNoon! Mr.Shelby")
            else:
             print(f"it's  Eveining! Mr.Shelby ")
             speak("it's eveining Mr.Shelby ")

        
        elif'good after Noon 'in query or 'good afternoon' in query or 'good afterNoon' in query:
           if hour>=12 and hour<18:
            speak("thank you Mr.Shelby")
            print("thank you Mr.Shelby")
            speak("best of luck for your work Mr.Shelby")
            print("best of luck for your work")
           else:
            speak("Mr.Shelby it's not afterNoon")
            print("Mr.Shelby it's not afterNoon")
            speak(f"Mr.Shelby the time is {strTime}")
            print(f"Mr.Shelby the time is {strTime}")
            speak("according to the time")
            print("according to the time")
            if hour>=0 and hour<12:
                speak("it's morning Mr.Shelby")
                print("it's morning Mr.Shelby")
            else:
                print("it's eveining Mr.Shelby")
                speak("it's eveining Mr.Shelby")

        elif'good evening'in query :
            speak("thank you Mr.Shelby")
            print("thank you Mr.Shelby")
            speak("what's your plan for evening Mr.Shelby")
            time.sleep(3)
            crlf = takecommand()
            if "nothing"in crlf or "no plans" in query:
                speak("i think you are taking rest")
                speak("that's good Mr.Shelby")
                speak("can i play some melodi songs for you Mr.Shelby")
                ln=takecommand()
                if"yes"in ln:
                    speak("that's nice")
                    speak("i make a playlist for you hope you like it")
                    webbrowser.open("https://www.youtube.com/watch?v=V-huZdv9ODQ&list=RDV-huZdv9ODQ")
                    speak("enjoy your evening Mr.Shelby")
                    speak("if you need any thing just call me")
                    time.sleep(60)
                else:
                    speak("no problem Mr.Shelby")
                    speak("if you need any thing just call me")
            else:
                speak("that's a good plan, Mr.Shelby")
                speak("if you need help just tell me i will help you")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif'youtube' in query:
           Query = query.replace("dodo", "")
           QUERY = Query.replace("youtube search","")
           from youtube import YouTubeSearch
           YouTubeSearch(query)
        
        elif'google' in query:
           import wikipedia as googleScrap
           query = query.replace("dodo","")
           query = query.replace("google search","")
           query = query.replace("google","")
           speak(f"this is what i found on the web Mr.Shelby")
           pywhatkit.search(query)
           try:
               result = googleScrap.summary(query,1)
               speak(result)
           except:
             speak(f"no data found Mr.Shelby")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            webbrowser.open("https://www.youtube.com/watch?v=aTWZNrR025U&list=RDA8biKYgEpl4&index=5")

        elif ' time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Mr.Shelby, the time is {strTime}")
        elif'date'in query:
            datae=datetime.date.today()
            speak(f"Mr.Shelby, today date is{datae}")

        elif 'open code' in query:
            codePath='"C:\\Users\\xpred\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
            os.startfile(codePath)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")    

        elif'hello' in query:
            speak(random.choice(GREETINGS_RES))

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak(f"opening youtube Mr.Shelby")

        elif 'open brave' in query:
            codePath="C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(codePath)
            speak("opening brave")

        elif'close the app' in query or 'close this app'in query or 'close this current app'in query or 'close the current app'in query:
            pyautogui.hotkey('alt','f4')
            speak("closing the currunt app Mr.Shelby")

        elif'shutdown'in query:
            speak("ok Mr.Shelby the system is shutdown in")
            os.system("shutdown -s -t 5")
            speak("5")
            speak("4")
            speak("3")
            speak("2")
            speak("1")
            speak("0")
             
        
        elif'restart'in query:
            speak("ok Mr.Shelby the system is restart in")
            os.system("shutdown -r -t 5") 
            speak("5")
            speak("4")
            speak("3")
            speak("2")
            speak("1")
            speak("0")
            
        
        elif'thank you' in query:
            speak(f"no problem Mr.Shelby")
            speak(f"it's my duty")
        
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
            speak(f"opening instagram")

        elif'new project' in query:
            speak("ok Mr.Shelby let me prepare system Mr.Shelby")
            codePath='"C:\\Users\\xpred\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
            os.startfile(codePath)
            speak("do you want to save this file Mr.Shelby")
            ye=takecommand()
            if 'save' in ye:
                speak("is that a python file Mr.Shelby")
                speak("or same thing else Mr.Shelby ")
                yt=takecommand()
                if 'Python'in yt:
                    speak("ok Mr.Shelby, now tell me Mr.Shelby which name do you want to save this file")
                    ii=pyautogui
                    
                    pyautogui.keyDown('ctrl')
                    pyautogui.keyDown('alt')
                    pyautogui.keyDown('win')
                    pyautogui.press('n')
                    go=takecommand()
                    name4=f"{go}.py"
                    ii.save(name4)
                    speak("the file has been save Mr.Shelby")
                elif'c'in yt or 'c plus plus ' in yt:
                    speak("ok Mr.Shelby, now tell me Mr.Shelby which name do you want to save this file")
                    eeeeeeee=pyautogui.__file__
                    re=takecommand()
                    uiuio=f"{re}.c"
                    eeeeeeee.save(uiuio)
                    speak("the file has been save Mr.Shelby")
                else:
                    speak("i can't do this Mr.Shelby right now")
                    speak("please tell me something else ")
        
        elif 'switch the window'in query or 'switch window' in query or 'change window' in query or 'change screen' in query:
            speak(f"okay Mr.Shelby, switching the window")
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        
       
        elif 'take screenshot' in query or "take a screenshot" in query or 'capture the screen'in query or 'take a ss'in query or 'take ss' in query:
            speak("by what name do you want me to save the screenshot?")
            name = takecommand()
            speak(f"alrightMr.Shelby, taking the screen shot")
            img = pyautogui.screenshot()
            name2 = f"{name}.png"
            img.save(name2)
            speak("The screenshot has been succesfully captured")

        elif "goodbye" in query or "offline"in query or "bye"in query or "i have to go " in query:
            speak(f"alright Mr.Shelby, going offline . it was nice working with you")
            sys.exit()

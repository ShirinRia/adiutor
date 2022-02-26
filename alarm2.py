import os
import datetime,time
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
import webbrowser,winsound
from playsound import playsound
def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
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
def bacao():
    speak("When do you want the alarm to ring? ")

    alarmH = int(input("What hour do you want the alarm to ring? "))
    alarmM = int(input("What minute do you want the alarm to ring? "))
    #amPm = str(input("am or pm? "))
    wh=datetime.datetime.now().hour-alarmH
    wm=datetime.datetime.now().minute-alarmM
    if(wh<0):
        wh=-1*wh
    if(wm<0):
        wm=-1*wm
    print("Alarm in",wh,"hours",wm,"minutes")
    for i in range(25):
        # print("j")
        # time.sleep(2)
        while True:
            if(alarmH == datetime.datetime.now().hour and
                alarmM == datetime.datetime.now().minute) :
                print("Time to wake up")
                # snz = str(input("Do you want to snooze? "))
                # playsound('ratsasan.mp3')
                winsound.Beep(5000, 250)
                # if 'Yes' in snz:
                #     sleep(60)
                #     playsound('ratsasan.mp3')
                break
            else:
                query = takeCommand().lower()
                if 'open youtube' in query:
                    webbrowser.open("https://www.youtube.com/")
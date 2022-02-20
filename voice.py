import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime,wikipedia #pip install wikipedia
import webbrowser,os,sys,wolframalpha
from requests import get
import smtplib
import cv2,random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
chromedir="C:\\Program Files (x86)\\chromedriver.exe"
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('efshitaria123@gmail.com', '123ri@2018016')
    server.sendmail('efshitaria123@gmail.com', to, content)
    server.close()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Adiutor, your virtual assistant. how may I help you?")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source: #microphone k source hishebe use korbe,
        print("Listening...")
        r.pause_threshold = 1 #(amar kothar kono part jeno shuna bad na jay
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


# if __name__ == "__main__":
def start_game():
    wishMe()
    while True:
        #result = input("input")
        query = takeCommand().lower()
        if 'open notepad' in query:
             path="C:\\Windows\\System32\\notepad.exe"
             os.startfile(path)

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'play music on device' in query:
            music_dir = 'G:\music'
            songs = os.listdir(music_dir)
            #print(songs)
            #rd=random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        #C:\\Users\\Hp\\Desktop\\Not use so much\\FastStone Capture
        # elif result:
        #     webbrowser.open("www.youtube.com")

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open Facebook' in query:
            webbrowser.open("facebook.com")

        #search google

        #send whatsapp msg

        #play youtubevideo

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "shirinsultana596@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")

        elif 'i have some question' in query:
            speak("ask me anything")
            query = takeCommand().lower()
            try:
                client = wolframalpha.Client("RUEEV7-36762W69XT")
                res = client.query(query)
                ans = next(res.results).text
                speak(ans)
                # Logic for executing tasks based on query
            except Exception:
                try:
                    results = wikipedia.summary(query, sentences=2)
                    speak(results)

                except Exception:
                    try:
                        webbrowser.open("https://www.google.com/search?q=" + query)
                    except Exception:
                        speak("It is weird but I got nothing")
        elif 'stop' in query:
            speak("Thanks for using me. Have a good day")
            sys.exit()
    # speak("Do you have any other work?")
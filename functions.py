import geocoder,psutil,pyautogui,webbrowser,os,sys,wolframalpha,pyjokes,speedtest,pywhatkit,requests,pyttsx3,datetime,wikipedia
from time import sleep
import speech_recognition as sr #pip install speechRecognition
from pywikihow import search_wikihow

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 175)
def news():
    main_url='https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=d67833a8153940f3aee155b122f04984'
    main_page=requests.get(main_url).json()
    articles = main_page["articles"]
    head=[]
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        print(f"today's {day[i]} news is {head[i]}")
        speak(f"today's top {day[i]} news is {head[i]}")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    time = datetime.datetime.now().strftime('%I %M %p')
    speak('Current Time Is' + time)
    speak("I am Adiutor, your virtual assistant. how may I help you?")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():

    battery = psutil.sensors_battery()
    percentage = battery.percent
    if percentage <= 40:
         speak("Don't have enough power to work, please connect to the charger")

    elif percentage <= 15 :
        speak("The system have very low power, please connect to charging otherwise the system will shutdown very soon")

    # It takes microphone input from the user and returns string output
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


def start_game():
    while True:
        query = takeCommand().lower()
        if 'open notepad' in query:
             path="C:\\Windows\\System32\\notepad.exe"
             os.startfile(path)
        elif 'close notepad' in query:
             os.system("taskkill /f /im notepad.exe")

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'play music on device' in query:
            music_dir = 'G:\music'
            songs = os.listdir(music_dir)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))

        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current Time Is' + time)
            print(time)

        elif 'joke' in query:
            result=pyjokes.get_joke(language="en", category="all")
            print(result)
            speak(result)

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("search", "")
            query = query.replace("on wikipedia", "")
            webbrowser.open("https://en.wikipedia.org/wiki/"+query)
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")
        elif 'open insta' in query:
            webbrowser.open("https://www.instagram.com/")
        elif 'open Facebook' in query:
            webbrowser.open("facebook.com")
        elif 'weather' in query:
           import weather
           weather.weather()
        #search google
        elif 'google search' in query:
            user = input("enter something to search")
            webbrowser.open("https://www.google.com/search?q=" + user)
        #play youtubevideo
        elif 'on youtube' in query:
            song = query.replace('play', '')
            song = query.replace('on youtube', '')
            print(song)
            speak('playing' + song)
            pywhatkit.playonyt(song)

        elif "internet speed" in query:
            st=speedtest.Speedtest()
            dl=round((st.download()/1000000),2)
            up=round((st.upload()/1000000),2)
            speak(f"you have {dl} mbps downloading speed and {up} mbps uploading speed")
        elif 'email' in query:
            try:
                import mail
                mail.est()
            except Exception as e:
                speak("Sorry, I am not able to send this email")

        elif "news" in query:
            speak("Please wait.Fetching the latest news")
            news()
        elif "read book" in query:
            import audiobooks
            audiobooks.audiobk()

        elif "where i am" in query or "where we are" in query or "track location" in query:
            speak("Wait, let me check")
            try:
                ipadd=requests.get('https://api.ipify.org/').text
                ip = geocoder.ip("me")
                print(ip.city)
                url='https://get.geojs.io/v1/ip/geo/'+ipadd+'.json'
                geo_requests=requests.get(url)
                geo_data=geo_requests.json()
                country=geo_data['country']
                print(f"I think we are in {ip.city} of {country}")
                speak(f"I think we are in {ip.city} of {country}")
            except Exception as e:
                speak("Sorry, Due to a network problem, I am unable to locate our location")

        elif "take screenshot" in query:
            speak("please tell me the name for this screenshot file")
            name=takeCommand().lower()
            speak("please hold the screen for few seconds, i am taking screenshot")
            sleep(3)
            img=pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("screenshot is saved")

        elif "how to do" in query:
            speak("How to do mode is activated.")
            while True:
                speak("Please tell me what you want to know")
                how=takeCommand().lower()
                try:
                    if "exit" in how or "close" in how:
                        speak("how to do mode is closed")
                        break
                    else:
                        max_result=1
                        how_to=search_wikihow(how,max_result)
                        assert len(how_to)==1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("Sorry, i am not able to find this")
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

        elif 'check battery' in query:
            battery=psutil.sensors_battery()
            percentage=battery.percent
            speak(f"Our system have {percentage} percent battery")
            if percentage>75:
                speak("We have enough power to continue our work")
            elif percentage>40 and percentage<=75:
                speak("You should connect the system to charging")
            elif percentage<=15 and percentage<=30:
                speak("Don't have enough power to work, please connect to the charger")
            elif percentage<=15:
                speak("The system have very low power, please connect to charging otherwise the system will shutdown very soon")

        elif 'volume up' in query:
            pyautogui.press("volumeup")
        elif 'volume down' in query:
            pyautogui.press("volumedown")
        elif 'volume mute' in query:
            pyautogui.press("volumemute")
        elif "shut down" in query:
            os.system("shutdown /s /t 5")

        elif "restart" in query:
            os.system("shutdown /r /t 5")

        elif "hide all files" in query or "hide folder" in query or "folder visible" in query:
            speak("are you sure you want hide all files?")
            condition=takeCommand().lower()
            if "yes" in condition:
                os.system("attrib +h /s /d")
                speak("Sir, all this files in this folder are now hidden")
            elif "visible" in condition or "no" in condition:
                os.system("attrib -h /s /d")
                speak("Sir, all this files in this folder are now visible")
            elif "leave it" in condition or "leave for now" in condition:
                speak("ok sir")

        elif "sleep" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif 'stop' in query:
            speak("Thanks for using me. Have a good day")
            sys.exit()

def begindfg():
    wishMe()
    start_game()

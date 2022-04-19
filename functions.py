import hashlib
from time import sleep
import socket,geocoder,psutil,pyautogui,mysql.connector,pyttsx3,pywhatkit,requests,datetime,wikipedia,webbrowser,os,sys,wolframalpha,pyjokes,speedtest
import speech_recognition as sr #pip install speechRecognition
from plyer import notification
from pywikihow import search_wikihow
mydb=mysql.connector.connect(
    host=" sql6.freemysqlhosting.net",
    user="sql6473246",
    password="vrYZb6cDv9",
    database="sql6473246"
)
commanddict= {}

if mydb.is_connected():
    cur = mydb.cursor()
    query = "select phone from Contacts where name=%s"
    name=("farhana",)
    cur.execute(query, name)
    fetch = cur.fetchall()

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
hash = hashlib.md5(IPAddr.encode())
haship=hash.hexdigest()

if mydb.is_connected():
    cur = mydb.cursor()
    query = "select * from Command where ip=%s"
    ip = (haship,)
    cur.execute(query, ip)
    fetch = cur.fetchall()
    for s in fetch:
        commanddict[s[1]] = [s[2],s[3]]

    keys_list = list(commanddict)


def music(c):
    os.startfile("G:\music\\" + c + ".mp3")

def h():
    os.startfile('G:\\code\\python\\adiutor\\timewidget.py')

def r():
    os.startfile('G:\\code\\python\\adiutor\\audiorecorder.py')
def g():
    os.startfile('G:\\code\\python\\adiutor\\automation.py')
def ad():
    import audiobook_gui
    audiobook_gui.showdialog()
def qr():
    import qr_gui
    qr_gui.showdialog()
def pl():
    import plagarism_gui
    plagarism_gui.showdialog()
def wishMe():
    battery = psutil.sensors_battery()
    percentage = battery.percent
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    ctime = datetime.datetime.now().strftime('%#I %M %p')
    speak('Current Time Is' + ctime)
    if percentage <= 40:
         speak("Don't have enough power to work, please connect to the charger")

    elif percentage <= 15 :
        speak("The system have very low power, please connect to charging otherwise the system will shutdown very soon")
    speak("I am Adiutor, your virtual assistant.")
    speak("do you want to activate chrome automation mode?")
    auto = takeCommand().lower()
    if 'yes' in auto:
        speak("Chrome automation mode activated")
        g()
    else:
        speak('Okay, how may I help you?')
def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 175)
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
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


def start_game(time_1):
    from time import time
    while True:
        time_2 = time()
        time_interval = time_2 - time_1
        if time_interval > 15000:
            time_1=time_2
            notification.notify(
                title="Please take a break",
                message="It's good to take short break after 25 minutes of work (as per the Pomodoro Techniqe)",
                timeout=10
            )
        query = takeCommand().lower()

        if query in keys_list:
            print("hai")
            path=commanddict[query][0]

            medium=commanddict[query][1]
            if 'System' in medium:
                os.system(path)
            elif 'Application' in medium:
                os.startfile(path)
            elif 'Website' in medium:
                 webbrowser.open(path)

        elif 'open command prompt' in query:
            os.system("start cmd")
        elif 'start recorder' in query:
            r()
        elif 'music on device' in query:
            speak("do you have any choice?")
            c=takeCommand().lower()
            if 'no' in c:
                music_dir = 'G:\music'
                songs = os.listdir(music_dir)
                #print(songs)
                #rd=random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song))

            else:
                c=c.replace("play",'')
                c=c.replace(" ","")
                music(c)

        elif 'time' in query:
            times = datetime.datetime.now().strftime('%I %M %p')
            speak('Current Time Is' + times)
            print(times)
        elif 'alarm' in query:
            h()
        elif 'joke' in query:
            result=pyjokes.get_joke(language="en", category="all")
            print(result)

            speak(result)

        elif 'google search' in query:

                user = query.replace("google search", "")

                speak(f"Searching {user} on google")

                pywhatkit.search(user)
                speak("This is what i found")


        elif 'youtube search' in query:
            user = query.replace("youtube search", "")
            print(user)
            webbrowser.open("https://www.youtube.com/results?search_query=" + user)

            speak(f"Searching {user} on youtube")
        elif 'wikipedia' in query:
            try:
                speak('Searching Wikipedia...')
                query = query.replace("search", "")
                query = query.replace("on wikipedia", "")
                webbrowser.open("https://en.wikipedia.org/wiki/"+query)
                results = wikipedia.summary(query, sentences=2)
                speak(f"According to Wikipedia {results}")
                print(results)
            except Exception as e:
                continue

        elif 'activate dictionary' in query:
            speak("Activated")

            prob=takeCommand().lower()
            if 'None' in prob or 'none' in prob:
                speak("Say again")

                prob = takeCommand().lower()
                import dict
                dict.dictionary(prob)
            else:
                import dict
                dict.dictionary(prob)

        elif 'activate chrome automation mode' in query:

            speak("Chrome automation mode activated")
            g()
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")
        elif 'open insta' in query:
            webbrowser.open("https://www.instagram.com/")
        elif 'open Facebook' in query:
            webbrowser.open("facebook.com")
        elif 'website' in query:
            query=query.replace("open","")
            query=query.replace("website","")
            query = query.replace(" ", "")
            web='https://www.'+query+'.com'
            webbrowser.open(web)
            speak("Launching")
        elif 'weather' in query:
           import weather
           weather.weather()

        #play youtubevideo
        elif 'on youtube' in query:
            song = query.replace('play', '')
            song = query.replace('on youtube', '')
            print(song)
            speak("do you want to activate youtube automation mode?")
            ch=takeCommand().lower()
            if 'yes' in ch:
                speak("Youtube automation mode activated")
                from automation import youtubeauto
                youtubeauto()
            elif 'no' in ch:
                speak("okay")
            speak('playing' + song)
            pywhatkit.playonyt(song)

        elif "internet speed" in query:
            st=speedtest.Speedtest()
            dl=round((st.download()/1000000),2)
            up=round((st.upload()/1000000),2)
            speak("Wait let me check")
            speak(f"you have {dl} mbps downloading speed and {up} mbps uploading speed")
        elif 'email' in query:
            try:
                import mailinterface
                mailinterface.showdialog()

            except Exception as e:
                speak("Sorry, I am not able to send this email")

        elif "top news" in query:
            speak("Please wait Fetching the latest news")
            from news import news
            news()
        elif "corona news" in query:
            speak("which country")
            query=takeCommand().lower()
            speak("Please wait Fetching the latest news")
            from news import corona
            corona(query)

        elif "read book" in query:
            ad()

        elif "qr code" in query:
            qr()
        elif "check copy" in query:
            pl()
        elif "download video" in query:
            import youtube_dwnloader
            youtube_dwnloader.showdialog()
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
            name=name+".png"
            path='E:\\'+name
            speak("please hold the screen for few seconds, i am taking screenshot")
            sleep(3)
            img=pyautogui.screenshot()
            img.save(path)
            speak("screenshot is saved here")
            os.startfile('E:\\')
        elif 'remember that' in query:
            remembermsg=query.replace("remember that","")
            speak(remembermsg)
            remember=open('data.txt','w')
            remember.write(remembermsg)
            remember.close()
        elif 'what do you remember' in query or "if i have any schedule today" in query or "reminder" in query:

            remember=open('data.txt','r')
            speak(remember.read())
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
            while True:
                query = takeCommand().lower()
                if 'none' not in query:
                    if 'exit' in query:
                        speak("Okay")
                        break
                    else:
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
                else:
                    speak("Ask again please")

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

        elif 'leave now' in query:
            speak("Thanks for using me. Have a good day")
            sys.exit()


def begindfg():
    from time import time
    time_1 = time()
    wishMe()
    start_game(time_1)

def begin_2():
    from time import time
    time_1 = time()
    start_game(time_1)

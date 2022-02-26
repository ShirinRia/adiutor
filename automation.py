import keyboard,pyttsx3
import speech_recognition as sr

def youtubeauto():
    comm = takeCommand().lower()
    if 'pause' in comm:
        keyboard.press('space')
    elif 'restart' in comm:
        keyboard.press('0')
    elif 'mute' in comm:
        keyboard.press('m')
    elif 'skip' in comm:
        keyboard.press('m')
    elif 'back' in comm:
        keyboard.press('l')
    elif 'full screen' in comm:
        keyboard.press('f')
    elif 'theater mode' in comm:
        keyboard.press('t')

def googleauto(query):
    if 'close this tab' in query:
        keyboard.press_and_release('ctrl+w')
    elif 'open new tab' in query:
        keyboard.press_and_release('ctrl+t')
    elif 'open new window' in query:
        keyboard.press_and_release('ctrl+n')
    elif 'history' in query:
        keyboard.press_and_release('ctrl+h')
    elif 'bookmark this tab' in query:
        keyboard.press_and_release('ctrl+d')
    elif 'refresh this tab' in query:
        keyboard.press_and_release('ctrl+r')
    elif 'Go to top of page' in query:
        keyboard.press_and_release('home')
    elif 'Go to bottom of page' in query:
        keyboard.press_and_release('end')

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

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 175)
    engine.say(audio)
    engine.runAndWait()
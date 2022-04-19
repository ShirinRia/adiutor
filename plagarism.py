from difflib import SequenceMatcher
import pyttsx3 #pip install pyttsx3

def plgrsm(f,g):
    with open(f,"rb") as file1,open(g,"rb") as file2:
        file1data=file1.read()
        file2data=file2.read()
        print(file1data)
        similarities=SequenceMatcher(None,file1data,file2data).ratio()
        print(str(round(similarities * 100)) + " percent similarities")
        speak(str(round(similarities*100))+" percent similarities")

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()



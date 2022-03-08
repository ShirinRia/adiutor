from difflib import SequenceMatcher
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# f="thesis.txt"
# g="prjct_bug.txt"

def plgrsm(f,g):
    # book=open(f,"rb")
    # book2=open(g,"rb")
    with open(f,"rb") as file1,open(g,"rb") as file2:
        file1data=file1.read()
        file2data=file2.read()
        print(file1data)
        similarities=SequenceMatcher(None,file1data,file2data).ratio()
        #speak(round(similarities*100))
        print(str(round(similarities * 100)) + " percent similarities")
        speak(str(round(similarities*100))+" percent similarities")



import sys,cv2,pyttsx3
import PyPDF2 as pdf
import pyttsx3 #pip install pyttsx3
import pywhatkit
import requests
import speech_recognition as sr #pip install speechRecognition
import datetime,wikipedia #pip install wikipedia
import webbrowser,os,sys,wolframalpha,pyjokes,keyboard

def printi():
    # print("boo")
    from voice import dfg
    dfg()
def audiobk():
    global engine
    engine = pyttsx3.init()
    try:
        getbk=input("path: ")
        book=open(getbk,"rb")
        pdfreader=pdf.PdfFileReader(book)
        pages=pdfreader.numPages
        print(pages)


        engine.say("From which page should I start reading?")
        engine.runAndWait()
        start_page=int(input("enter:  "))
        for i in range(start_page,pages+1):

            pageget=pdfreader.getPage(i)
            text=pageget.extractText()
            engine.say(text)
            engine.runAndWait()

    except KeyboardInterrupt:
        # print("hi")
        engine.stop()
        printi()
audiobk()
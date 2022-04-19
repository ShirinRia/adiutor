import speech_recognition as sr
import pyttsx3
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from mailjet_rest import Client

api_key = '1662f0c8b4c265e18ef7186bdb724ad6'
api_secret = '46b648f8215a0fee6a8e6e4aa0dde148'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')
grid=QGridLayout()

def speak(audio):
  engine = pyttsx3.init('sapi5')
  voices = engine.getProperty('voices')
  engine.setProperty('voice', voices[0].id)
  engine.say(audio)
  engine.runAndWait()

def takeCommand():
  r = sr.Recognizer()
  with sr.Microphone() as source:  # microphone k source hishebe use korbe,
    print("Listening...")
    r.pause_threshold = 1  # (amar kothar kono part jeno shuna bad na jay
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

def showdialog():
   dlg = QDialog()
   dlg.setLayout(grid)
   groupbox = QGroupBox("Compose mail")

   vbox = QVBoxLayout()
   groupbox.setLayout(vbox)
   labelcmnd = QLabel("Enter Mail Address")

   cmnd = QLineEdit()
   cmnd.setStyleSheet("border:1px solid '#BC006C'; margin:0 20px 70px; padding: 5px 0 5px;")

   print(cmnd.text())

   btn = QPushButton('OK')
   btn.setStyleSheet(
      "*{width: 100px;" +
      "height:10px;" +
      "border:2px solid '#BC006C';" +
      "border-radius: '15px';" +
      "font-size: 60 px;" +
      "color:'Black';" +
      "margin:0px 150px 70px;"
      "padding: 8px 15px}" +
      "*:hover{background:'#BC006C';color:'White';}"
   )
   btn.clicked.connect(lambda: button_click(cmnd.text()))

   vbox.addWidget(labelcmnd)
   vbox.addWidget(cmnd)
   vbox.addWidget(btn)
   grid.addWidget(groupbox, 0, 0)
   dlg.setWindowTitle("Dialog")
   dlg.setFixedWidth(500)
   dlg.setFixedHeight(300)
   dlg.setWindowModality(Qt.ApplicationModal)
   dlg.exec_()


def button_click(a):
   to = a
   speak("What should I say?")
   content = takeCommand().capitalize()
   if 'none' in content or 'None' in content:
      speak("Say again please")
      content = takeCommand().capitalize()
      if 'dot' in content:
         content = content.replace(" dot", ".")
      if 'question mark' in content:
         content = content.replace(" question mark", "?")
      if 'comma' in content:
         content = content.replace(" comma", ",")
      if 'exclamation mark' in content:
         content = content.replace(" exclamation mark", "!")
      print(content)
      data = {
         'Messages': [
            {
               "From": {
                  "Email": "efshitaria123@gmail.com",
                  "Name": "no reply"
               },
               "To": [
                  {
                     "Email": to,
                     "Name": ""
                  }
               ],
               "Subject": "Testing",
               "TextPart": "My first python email",
               "HTMLPart": f"<h3>{content} </h3>",
               "CustomID": "AppGettingStartedTest"
            }
         ]
      }
      result = mailjet.send.create(data=data)
      res = result.json()
      temp_stt = ((res['Messages'][0]))
      temp_stt = ((temp_stt['Status']))
      if 'success' in temp_stt:
         speak("Email has been sent!")
         return 0
      else:
         speak("I can not send email!")
   else:
      if 'dot' in content:
         content = content.replace(" dot", ".")
      if 'question mark' in content:
         content = content.replace(" question mark", "?")
      if 'comma' in content:
         content = content.replace(" comma", ",")
      if 'exclamation mark' in content:
         content = content.replace(" exclamation mark", "!")
      print(content)
      data = {
         'Messages': [
            {
               "From": {
                  "Email": "efshitaria123@gmail.com",
                  "Name": "no reply"
               },
               "To": [
                  {
                     "Email": to,
                     "Name": ""
                  }
               ],
               "Subject": "Testing",
               "TextPart": "My first python email",
               "HTMLPart": f"<h3>{content} </h3>",
               "CustomID": "AppGettingStartedTest"
            }
         ]
      }
      result = mailjet.send.create(data=data)
      res = result.json()
      temp_stt = ((res['Messages'][0]))
      temp_stt = ((temp_stt['Status']))
      if 'success' in temp_stt:
         speak("Email has been sent!")
         return 0
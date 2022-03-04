import sys, pyttsx3
import speech_recognition as sr
from PyQt5.QtWidgets import QInputDialog, QWidget, QApplication
from mailjet_rest import Client

api_key = ''
api_secret = ''
mailjet = Client(auth=(api_key, api_secret), version='v3.1')


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


class Example(QWidget):

  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    # Add button
    text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter text:')
    if ok:
      mail (text)

def mail(to):
  speak("To whom")

  to=to.replace(" ", "")+"@gmail.com"
  print(to)
  speak("What should I say?")
  content = takeCommand().capitalize()
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
  print (result.status_code)
  print (result.json())
  speak("Email has been sent!")
def est():
  app = QApplication(sys.argv)
  to=Example()
est()
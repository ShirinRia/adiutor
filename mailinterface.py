import sys
from PyQt5.QtWidgets import *
from mailjet_rest import Client
import pyttsx3
import speech_recognition as sr


mailjet = Client(auth=(api_key, api_secret), version='v3.1')

app=QApplication(sys.argv)
window=QWidget()
# window.setWindowFlag(Qt.FramelessWindowHint)
window.setWindowTitle("Adiutor")
window.setFixedWidth(500)
window.setFixedHeight(300)
window.move(440,80)#(x,y)
window.setStyleSheet("background:'white'")
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

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setLayout(grid)
        groupbox = QGroupBox("Compose mail")

        vbox = QVBoxLayout()
        groupbox.setLayout(vbox)
        labelcmnd=QLabel("Enter Mail Address")

        cmnd = QLineEdit(self)
        cmnd.setStyleSheet("border:1px solid '#BC006C'; margin:0 20px 70px; padding: 5px 0 5px;"  )

        print(cmnd.text())

        btn = QPushButton('Add Command')
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

def button_click(a):
    to = a
    print(to)
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
        print(result.status_code)
        print(result.json())
        res=result.json()
        temp_city = ((res['Messages'][0]))

        print(temp_city)
        temp_city = ((temp_city['Status']))
        print(temp_city)
        if 'success' in temp_city:
         speak("Email has been sent!")
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
        print(result.status_code)
        print(result.json())
        res = result.json()
        temp_city = ((res['Messages'][0]))

        print(temp_city)
        temp_city = ((temp_city['Status']))
        print(temp_city)
        if 'success' in temp_city:
            speak("Email has been sent!")
            return 0

def est():
    screen = Window()
    window.setLayout(grid)
    window.show()
    # sys.exit(app.exec())
est()
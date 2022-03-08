import sys
from PyQt5.QtWidgets import *
from mailjet_rest import Client
import pyttsx3
import speech_recognition as sr



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
        groupbox = QGroupBox("Qr Code Generator")

        vbox = QVBoxLayout()
        groupbox.setLayout(vbox)
        labelcmnd=QLabel("Enter your link")

        cmnd = QLineEdit(self)
        cmnd.setStyleSheet("border:1px solid '#BC006C'; margin:0 20px 50px; padding: 5px 0 5px;"  )


        print(cmnd.text())

        btn = QPushButton('OK')
        btn.setStyleSheet(
            "*{width: 100px;" +
            "height:10px;" +
            "border:2px solid '#BC006C';" +
            "border-radius: '15px';" +
            "font-size: 60 px;" +
            "color:'Black';" +
            "margin:0px 150px 20px;"
            "padding: 8px 15px}" +
            "*:hover{background:'#BC006C';color:'White';}"
        )
        btn.clicked.connect(lambda: button_click(cmnd.text(),))

        vbox.addWidget(labelcmnd)
        vbox.addWidget(cmnd)

        vbox.addWidget(btn)
        grid.addWidget(groupbox, 0, 0)

def button_click(a):
    to = a
    print(to)
    import qr
    qr.qrcd(to)
screen = Window()
window.setLayout(grid)
window.show()
sys.exit(app.exec())
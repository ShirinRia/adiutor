import sys,datetime,wikipedia,smtplib,cv2,random,pyttsx3
# from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, \
#     QMainWindow, QHBoxLayout, QAction, QPlainTextEdit, QMenuBar, QTabWidget, QListWidgetItem, QListWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt
from PIL import Image
import speech_recognition as sr #pip install speechRecognition
from requests import get
import webbrowser

widgets = {
    "logo": [],
    "button": [],
    "items": [],
    "question": [],
    "answer1": [],
    "answer2": [],
    "answer3": [],
    "answer4": []
}

app=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle("Adiutor")
window.setFixedWidth(500)
window.setFixedHeight(600)
window.move(440,80)#(x,y)
window.setStyleSheet("background:'White'")
grid=QGridLayout()
frm=QFormLayout()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Adiutor, your virtual assistant. how may I help you?")

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    #It takes microphone input from the user and returns string output

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
    '''display frame 2'''

    wishMe()
    while True:
        query = takeCommand().lower()
        if 'open youtube' in query:

            webbrowser.open("https://www.youtube.com/")
        elif 'set alarm' in query:
                import alarm2
                alarm2.bacao()


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setLayout(grid)
        label1 = QLabel("Widget in Tab 1.")
        label3 = QLabel("Widget in Tab 3.")
        label4 = QLabel("Widget in Tab 4.")
        label1.setStyleSheet("color:'Green';")
        list_widget = QListWidget()
        list_widget2 = QListWidget()
        i=1
        item1 = QListWidgetItem("Hello dear, Welcome to Adiutor.")
        item2 = QListWidgetItem("Read the following instructions to run adiutor as you want:")
        item3 = QListWidgetItem("Default commands :")
        item4 = QListWidgetItem("   " +str(i) + " " + "open youtube (For opening youtube)")
        item5 = QListWidgetItem("   " +str(i+1) + " " +" open google (For opening google)")
        item6 = QListWidgetItem("   " +str(i+2) + " " +" open facebook (For opening facebook)")
        item7 = QListWidgetItem("   " +str(i+3) + " " +" open instagram (For opening instagram)")
        item8 = QListWidgetItem("   " +str(i+4) + " " +" search .. on google (for searching anything on google)")
        item9 = QListWidgetItem("   " +str(i+5) + " " +" play ... on youtube (for playing music on youtube)")


        list_widget.addItem(item1)
        list_widget.addItem(item2)
        list_widget.addItem(item3)
        list_widget.addItem(item4)
        list_widget.addItem(item5)
        list_widget.addItem(item6)
        list_widget.addItem(item7)
        list_widget.addItem(item8)
        list_widget.addItem(item9)

        list_widget.setWordWrap(True)

        list_widget.setStyleSheet("color:'Green'; font-size: 16px; ")
        #
        # text = QListWidgetItem(QInputDialog.getText(self, 'Input Dialog', 'Enter text:'))
        # list_widget2.addItem(text)
        btn = QPushButton('Add Command')
        btn.setStyleSheet(
            "*{width: 100px;" +
            "height:10px;" +
            "border:2px solid '#BC006C';" +
            "border-radius: '15px';" +
            "font-size: 60 px;" +
            "color:'Black';" +
            "margin:0px 150px 100px;"
            "padding: 8px 15px}" +
            "*:hover{background:'#BC006C';color:'White';}"
        )
        btn.clicked.connect(self.showDialog)
        groupbox = QGroupBox("Customize Your Adiutor")

        vbox = QVBoxLayout()
        groupbox.setLayout(vbox)
        labelcmnd=QLabel("Command")
        labelpath=QLabel("Path/URL")
        cmnd = QLineEdit(self)
        cmnd.move(800, 20)
        path=QLineEdit(self)
        cmnd.setStyleSheet("border:1px solid '#BC006C'; margin:0 50px 20px; padding: 5px 0 5px;"  )
        labelpath.setStyleSheet("margin:0 0 0; ")
        path.setStyleSheet("border:1px solid '#BC006C'; margin:0 50px 100px; padding: 5px 0 5px;")
        vbox.addWidget(labelcmnd)
        vbox.addWidget(cmnd)
        vbox.addWidget(labelpath)
        vbox.addWidget(path)
        vbox.addWidget(btn)
        tabwidget = QTabWidget()
        tabwidget.addTab(label1, "Home")
        tabwidget.addTab(list_widget, "Help")
        tabwidget.addTab(groupbox, "Settings")
        tabwidget.addTab(label4, "List")
        grid.addWidget(tabwidget, 0, 0)
    def showDialog(self):
        text=QLineEdit(self)


# logo widget
image = QPixmap("microphone.png")
# image = image.scaledToWidth(100)
# image = image.scaledToHeight(100)
button = QPushButton()
# logo = QLabel()
# logo.setPixmap(image)
# logo.setAlignment(QtCore.Qt.AlignCenter)
# logo.setStyleSheet(" margin-bottom: 30px;")
button.setIcon(QIcon(image))
button.setIconSize(QtCore.QSize(100,100))
button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
button.setStyleSheet(
    "*{width: 100px;" +
    "height:100px;" +
    "border:2px solid '#BC006C';" +
    "border-radius: '15px';" +
    "font-size: 60 px;" +
    "color:'white';" +
    "margin:0px 170px 45px;}" +
    "*:hover{background:'#BC006C';}"
)
button.clicked.connect(start_game)
grid.addWidget(button, 4, 0, 1, 2)

def scndintrfc():

    screen = Window()
    window.setLayout(grid)
    window.show()
#     sys.exit(app.exec())
# scndintrfc()

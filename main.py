import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, \
    QMainWindow, QHBoxLayout, QAction, QPlainTextEdit, QMenuBar, QTabWidget, QListWidgetItem, QListWidget
from PyQt5.QtGui import QPixmap,QFont
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt
from PIL import Image

widgets = {
    "logo": [],
    "button": [],
    "score": [],
    "question": [],
    "answer1": [],
    "answer2": [],
    "answer3": [],
    "answer4": []
}
app=QApplication(sys.argv)
window=QWidget()
window.setWindowFlag(Qt.FramelessWindowHint)
window.setWindowTitle("Adiutor")
window.setFixedWidth(500)
window.setFixedHeight(300)
window.move(440,80)#(x,y)
window.setStyleSheet("background:#161219")
grid=QGridLayout()
image=QPixmap("logo2.png")
logo=QLabel()
def clear_widgets():
    ''' hide all existing widgets and erase
        them from the global dictionary'''
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        # for i in range(0, len(widgets[widget])):
        #     widgets[widget].pop()
def start_game():
    '''display frame 2'''
    clear_widgets()
    frame3()
def create_buttons(answer, l_margin, r_margin):
    '''create identical buttons with custom left & right margins'''
    button = QPushButton(answer)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setFixedWidth(200)
    button.setStyleSheet(
        #setting variable margins
        "*{margin-left: " + str(l_margin) +"px;"+
        "margin-right: " + str(r_margin) +"px;"+
        '''
        width:50px;
        height:50px;
        border: 2px solid '#BC006C';
        color: white;
        font-family: 'shanti';
        font-size: 16px;
        border-radius: 15px;
        padding: 33px 0;
        margin-top: 20px}
        *:hover{
            background: '#BC006C'
        }
        '''
    )
    # button.clicked.connect(show_frame1)
    return button
def frame1():
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top:30px;")
    widgets["logo"].append(logo)
    #button
    button=QPushButton("Start")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        "*{width: 30px;" +
        "height:30px;" +
        "border:2px solid '#BC006C';" +
        "border-radius: '15px';" +
        "font-size: 30 px;" +
        "color:'white';" +
        "margin:0px 170px 45px;}" +
        "*:hover{background:'#BC006C';}"
    )
    button.setFont(QFont('Raleway', 14))
    button.clicked.connect(start_game)
    widgets["button"].append(button)
    grid.addWidget(widgets["logo"][-1],0,0,1,2)#rowvalue,column value
    grid.addWidget(widgets["button"][-1],1,0,1,2)#rowvalue,column value

frame1()

def frame2():
     button = QPushButton("Login")
    # button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    # button.setStyleSheet(
    #     "*{width: 30px;" +
    #     "height:30px;" +
    #     "border:2px solid '#BC006C';" +
    #     "border-radius: '15px';" +
    #     "font-size: 30 px;" +
    #     "color:'white';" +
    #     "margin:0px 170px 45px;}" +
    #     "*:hover{background:'#BC006C';}"
    # )
    # button.setFont(QFont('Raleway', 14))
    # button.clicked.connect(start_game)
    # widgets["button"].append(button)
    # grid.addWidget(widgets["logo"][-1], 0, 0, 1, 2)  # rowvalue,column value
    # grid.addWidget(widgets["button"][-1], 1, 0, 1, 2)  # rowvalue,column value


def frame3():
    window.setFixedWidth(500)
    window.setFixedHeight(600)
    window.move(440, 80)  # (x,y)
    window.setStyleSheet("background:'White'")
    label1 = QLabel("Widget in Tab 1.")
    label3 = QLabel("Widget in Tab 3.")
    label4 = QLabel("Widget in Tab 4.")
    list_widget = QListWidget()
    i = 1
    item1 = QListWidgetItem("Hello dear, Welcome to Adiutor.")
    item2 = QListWidgetItem("Read the following instructions to run adiutor as you want:")
    item3 = QListWidgetItem("Default commands :")
    item4 = QListWidgetItem("   " + str(i) + " " + "open youtube (For opening youtube)")
    item5 = QListWidgetItem("   " + str(i + 1) + " " + " open google (For opening google)")
    item6 = QListWidgetItem("   " + str(i + 2) + " " + " open facebook (For opening facebook)")
    item7 = QListWidgetItem("   " + str(i + 3) + " " + " open instagram (For opening instagram)")
    item8 = QListWidgetItem("   " + str(i + 4) + " " + " search .. on google (for searching anything on google)")
    item9 = QListWidgetItem("   " + str(i + 5) + " " + " play ... on youtube (for playing music on youtube)")

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
    tabwidget = QTabWidget()
    tabwidget.addTab(label1, "Home")
    tabwidget.addTab(list_widget, "Help")
    tabwidget.addTab(label3, "Settings")
    tabwidget.addTab(label4, "List")
    grid.addWidget(tabwidget, 0, 0)

    # logo widget
    image = QPixmap("microphone.jpg")
    image = image.scaledToWidth(100)
    image = image.scaledToHeight(100)
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet(" margin-bottom: 30px;")
    grid.addWidget(logo, 4, 0, 1, 2)


window.setLayout(grid)
window.show()
sys.exit(app.exec())
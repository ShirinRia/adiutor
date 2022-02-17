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
def start_gme():
    '''display frame 2'''
    clear_widgets()
    window.hide()
    import main
    main.scndintrfc()

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
    button.clicked.connect(start_gme)
    widgets["button"].append(button)
    grid.addWidget(widgets["logo"][-1],0,0,1,2)#rowvalue,column value
    grid.addWidget(widgets["button"][-1],1,0,1,2)#rowvalue,column value

frame1()

window.setLayout(grid)
window.show()
sys.exit(app.exec())
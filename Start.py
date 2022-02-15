import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap,QFont
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt
widgets={
    "logo":[],
    "button":[]
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
    widgets["button"].append(button)
    grid.addWidget(widgets["logo"][-1],0,0)#rowvalue,column value
    grid.addWidget(widgets["button"][-1],1,0)#rowvalue,column value

frame1()

window.setLayout(grid)
window.show()
sys.exit(app.exec())
import sys,datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from playsound import playsound

app=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle("Adiutor")
window.setFixedWidth(500)
window.setFixedHeight(300)
window.move(440,80)#(x,y)
grid=QGridLayout()

def p(d):
    window.hide()

    print(d)
    t3 = datetime.datetime.now().strftime("%#I:%M %p")
    print(t3)
    while True:
        t3 = datetime.datetime.now().strftime("%#I:%M %p")
        # print(t3)
        if(d==t3) :
            print("Time to wake up")
            playsound('ratsasan.mp3')
            break
        else:
            print("hi")

    # method for components
def UiComponents():
# creating a QDateTimeEdit widget
    t1=datetime.datetime.now().hour
    t2=datetime.datetime.now().minute
    print(t1)
    print(t2)
    print(datetime.datetime.now())
    datetimeedit = QTimeEdit()
    # time
    time = QTime(t1,t2)

    # setting only time
    datetimeedit.setTime(time)
    datetimeedit.setStyleSheet( "height:30px;border:2px solid '#BC006C';font-size: 30 px;color:'Black';")
    # creating a push button
    push = QPushButton("Ok")
    push.setStyleSheet(
            "*{width: 30px;" +
            "height:30px;" +
            "border:2px solid '#BC006C';" +
            "border-radius: '15px';" +
            "font-size: 30 px;" +
            "color:'Black';" +
            "margin:0px 170px 45px;}" +
            "*:hover{background:'#BC006C';color:'white';}"
        )
    push.setFont(QFont('Raleway', 14))

    # adding action to the push button
    push.clicked.connect(lambda : p(datetimeedit.text()))
    grid.addWidget(datetimeedit)#rowvalue,column value
    grid.addWidget(push)#rowvalue,column value

UiComponents()
window.setLayout(grid)
window.show()
sys.exit(app.exec())
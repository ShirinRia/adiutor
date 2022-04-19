from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,datetime
from playsound import playsound
grid=QGridLayout()

def window():
   app = QApplication(sys.argv)
   showdialog()
   sys.exit(app.exec_())


def p(d):
   t3 = datetime.datetime.now().strftime("%#I:%M %p")

   while True:
      t3 = datetime.datetime.now().strftime("%#I:%M %p")
      if (d == t3):
         playsound('ratsasan.mp3')
         break

def showdialog():
   dlg = QDialog()
   dlg.setLayout(grid)
   t1 = datetime.datetime.now().hour
   t2 = datetime.datetime.now().minute
   datetimeedit = QTimeEdit()
   time = QTime(t1, t2)
   # setting only time
   datetimeedit.setTime(time)
   datetimeedit.setStyleSheet(
      "height:30px;" +
      "border:2px solid '#BC006C';" +
      "font-size: 30 px;" +
      "color:'Black';"

   )
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
   push.clicked.connect(lambda: p(datetimeedit.text()))
   grid.addWidget(datetimeedit)  # rowvalue,column value
   grid.addWidget(push)  # rowvalue,column value
   dlg.setWindowTitle("Dialog")
   dlg.setFixedWidth(500)
   dlg.setFixedHeight(300)
   dlg.setWindowModality(Qt.ApplicationModal)
   dlg.exec_()

window()

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
grid=QGridLayout()

def showdialog():
   dlg = QDialog()
   dlg.setLayout(grid)
   groupbox = QGroupBox("Qr Code Generator")

   vbox = QVBoxLayout()
   groupbox.setLayout(vbox)
   labelcmnd = QLabel("Enter your link")

   cmnd = QLineEdit()
   cmnd.setStyleSheet("border:1px solid '#BC006C'; margin:0 20px 50px; padding: 5px 0 5px;")

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
   btn.clicked.connect(lambda: button_click(cmnd.text(), ))

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
   print(to)
   import qr
   qr.qrcd(to)
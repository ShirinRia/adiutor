from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
grid=QGridLayout()


def dialog():
   file, check = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()",
                                             "", "All Files (*);;Python Files (*.py);;Text Files (*.txt)")
   if check:
      global k
      k = file
      print(file)
      cmnd.setText(k)


def showdialog():
   dlg = QDialog()
   dlg.setLayout(grid)
   groupbox = QGroupBox("Audiobook")

   vbox = QVBoxLayout()
   groupbox.setLayout(vbox)
   labelcmnd = QLabel("Choose your book")

   global cmnd
   cmnd = QLineEdit()
   btn1 = QPushButton('Browse')
   btn1.setStyleSheet(
      "*{width: 10px;" +
      "height:100px;" +
      "border:2px solid '#BC006C';" +

      "font-size: 60 px;" +
      "color:'Black';" +
      "margin:0px 180px 24px 180px;" +
      "padding: 2px 2px; }" +
      "*:hover{background:'#BC006C';color:'White';}"
   )
   btn1.clicked.connect(dialog)
   cmnd.setStyleSheet("border:1px solid '#BC006C'; margin:0 20px 20px; padding: 5px 0 5px;")
   pglvl = QLabel("From which page should I start reading?")
   pg = QLineEdit()
   pg.setStyleSheet("border:1px solid '#BC006C'; margin:0 20px 20px; padding: 5px 0 5px;")
   #
   # print(cmnd.text())
   #
   btn = QPushButton('OK')
   btn.setStyleSheet(
      "*{width: 100px;" +
      "height:10px;" +
      "border:2px solid '#BC006C';" +
      "border-radius: '15px';" +
      "font-size: 60 px;" +
      "color:'Black';" +
      "margin:0px 130px 10px;" +
      "padding: 8px 15px}" +
      "*:hover{background:'#BC006C';color:'White';}"
   )
   btn.clicked.connect(lambda: button_click(cmnd.text(), pg.text()))
   #
   vbox.addWidget(labelcmnd)
   vbox.addWidget(cmnd)

   vbox.addWidget(btn1)
   vbox.addWidget(pglvl)
   vbox.addWidget(pg)
   vbox.addWidget(btn)
   grid.addWidget(groupbox, 0, 0)
   dlg.setWindowTitle("Dialog")
   dlg.setFixedWidth(500)
   dlg.setFixedHeight(300)
   dlg.setWindowModality(Qt.ApplicationModal)
   dlg.exec_()


def button_click(a, b):
   to = a
   page = b
   print(to)
   import audiobooks
   audiobooks.audiobk(to, page)
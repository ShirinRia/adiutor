import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
grid=QGridLayout()

def dialog1():
    file, check = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()",
                                              "", "All Files (*);;Python Files (*.py);;Text Files (*.txt)")
    if check:
        global s
        s=file
        print(file)
        pg.setText(s)

def dialog():
    file, check = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()",
                                              "", "All Files (*);;Python Files (*.py);;Text Files (*.txt)")
    if check:
        global k
        k=file
        print(file)
        cmnd.setText(k)

def showdialog():
   dlg = QDialog()
   dlg.setLayout(grid)
   groupbox = QGroupBox("Plagarism Checker")

   vbox = QVBoxLayout()
   groupbox.setLayout(vbox)
   labelcmnd = QLabel("Choose first file")
   global cmnd
   cmnd = QLineEdit()
   btn1 = QPushButton('Browse')
   btn1.setStyleSheet(
      "*{width: 10px;" +
      "height:100px;" +
      "border:2px solid '#BC006C';" +

      "font-size: 60 px;" +
      "color:'Black';" +
      "margin:0px 180px 20px 180px;" +
      "padding: 2px 2px; }" +
      "*:hover{background:'#BC006C';color:'White';}"
   )
   btn1.clicked.connect(dialog)

   cmnd.setStyleSheet("border:1px solid '#BC006C'; margin:0 20px 20px; padding: 5px 0 5px;")
   pglvl = QLabel("Choose second file?")
   global pg
   pg = QLineEdit()
   pg.setStyleSheet("border:1px solid '#BC006C'; margin:0 20px 20px; padding: 5px 0 5px;")

   btn2 = QPushButton('Browse')
   btn2.setStyleSheet(
      "*{width: 10px;" +
      "height:100px;" +
      "border:2px solid '#BC006C';" +

      "font-size: 60 px;" +
      "color:'Black';" +
      "margin:0px 180px 20px 180px;" +
      "padding: 2px 2px; }" +
      "*:hover{background:'#BC006C';color:'White';}"
   )
   btn2.clicked.connect(dialog1)
   print(cmnd)

   btn = QPushButton('OK')
   btn.setStyleSheet(
      "*{width: 100px;" +
      "height:10px;" +
      "border:2px solid '#BC006C';" +
      "border-radius: '15px';" +
      "font-size: 60 px;" +
      "color:'Black';" +
      "margin:0px 130px 15px;" +
      "padding: 8px 15px}" +
      "*:hover{background:'#BC006C';color:'White';}"
   )
   btn.clicked.connect(lambda: button_click(cmnd.text(), pg.text()))

   vbox.addWidget(labelcmnd)
   vbox.addWidget(cmnd)
   vbox.addWidget(btn1)
   vbox.addWidget(pglvl)
   vbox.addWidget(pg)
   vbox.addWidget(btn2)
   vbox.addWidget(btn)
   grid.addWidget(groupbox, 0, 0)
   dlg.setWindowTitle("Dialog")
   dlg.setFixedWidth(500)
   dlg.setFixedHeight(350)
   dlg.setWindowModality(Qt.ApplicationModal)
   dlg.exec_()


def button_click(a, b):
   to = a
   page = b
   print(to)
   import plagarism
   plagarism.plgrsm(to, page)

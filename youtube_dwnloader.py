import sys
from pytube import YouTube
import tkinter as tk
from tkinter import filedialog,messagebox
import pytube
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
grid=QGridLayout()
def dialog(self):
   download_Directory = filedialog.askdirectory(initialdir="E:/", title="Save Video")

   global download_path
   download_path=download_Directory
   print(download_path)
   cmnd.setText(download_path)


# def window():
#    app = QApplication(sys.argv)
#    w = QWidget()
#    btn = QPushButton(w)
#    btn.setText("Hello World!")
#    btn.move(100,50)
#    btn.clicked.connect(showdialog)
#    w.setWindowTitle("PyQt Dialog demo")
#    w.show()
#    sys.exit(app.exec_())
def showdialog():
   dlg = QDialog()
   dlg.setLayout(grid)
   groupbox = QGroupBox("Destination")
   v1=QHBoxLayout()
   groupbox.setLayout(v1)
   global cmnd

   cmnd = QLineEdit()
   cmnd.setStyleSheet("border:1px solid '#BC006C'; margin:0 20px 20px; padding: 5px 0 5px;")

   btn1 = QPushButton('Browse')
   btn1.setStyleSheet(
      "*{width: 50px;" +
      "height:15px;" +
      "border:2px solid '#BC006C';" +

      "font-size: 60 px;" +
      "color:'Black';" +
      "margin:0px 20px 20px 0px;" +
      "padding: 5px 5px; }" +
      "*:hover{background:'#BC006C';color:'White';}"
   )
   btn1.clicked.connect(dialog)

   v1.addWidget(cmnd)
   v1.addWidget(btn1)

   groupbox2 = QGroupBox("Enter Link")
   v1 = QVBoxLayout()
   groupbox2.setLayout(v1)

   global path
   path = QLineEdit()
   path.setStyleSheet("border:1px solid '#BC006C'; margin:0 20px 20px; padding: 5px 0 5px;")
   v1.addWidget(path)

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
   btn.clicked.connect(lambda: button_click(cmnd.text(),path.text()))

   grid.addWidget(groupbox2, 0, 0)
   grid.addWidget(groupbox, 1, 0)
   grid.addWidget(btn, 2, 0)
   dlg.setWindowTitle("Dialog")
   dlg.setFixedWidth(500)
   dlg.setFixedHeight(300)
   dlg.setWindowModality(Qt.ApplicationModal)
   dlg.exec_()


def button_click(a,b):
   SAVE_PATH = a
   link=b
   yt = pytube.YouTube(link)
   stream = yt.streams.first()
   stream.download(SAVE_PATH)
   messagebox.showinfo("SUCCESSFULLY","DOWNLOADED AND SAVED IN\n"+ SAVE_PATH)

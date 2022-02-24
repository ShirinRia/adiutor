import hashlib
import sys,mysql.connector,datetime,wikipedia,smtplib,cv2,random,pyttsx3,webbrowser,socket
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
hash = hashlib.md5(IPAddr.encode())
haship=hash.hexdigest()
db=mysql.connector.connect(
    host=" sql6.freemysqlhosting.net",
    user="sql6473246",
    password="vrYZb6cDv9",
    database="sql6473246"
)

app=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle("Adiutor")
window.setFixedWidth(500)
window.setFixedHeight(600)
window.move(440,80)#(x,y)
window.setStyleSheet("background:'White'")
grid=QGridLayout()


def start():
    import functions
    functions.begindfg()

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

        groupbox = QGroupBox("Customize Your Adiutor")

        vbox = QVBoxLayout()
        groupbox.setLayout(vbox)
        labelcmnd=QLabel("Command")
        labelpath=QLabel("Path/URL")
        cmnd = QLineEdit(self)
        path=QLineEdit(self)
        cmnd.setStyleSheet("border:1px solid '#BC006C'; margin:0 50px 20px; padding: 5px 0 5px;"  )
        labelpath.setStyleSheet("margin:0 0 0; ")
        path.setStyleSheet("border:1px solid '#BC006C'; margin:0 50px 100px; padding: 5px 0 5px;")
        print(cmnd.text())
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
        btn.clicked.connect(lambda: button_click(cmnd.text(),path.text()))

        vbox.addWidget(labelcmnd)
        vbox.addWidget(cmnd)
        vbox.addWidget(labelpath)
        vbox.addWidget(path)
        vbox.addWidget(btn)

        #table
        self.createTable()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        tabwidget = QTabWidget()
        tabwidget.addTab(label1, "Home")
        tabwidget.addTab(list_widget, "Help")
        tabwidget.addTab(groupbox, "Settings")
        tabwidget.addTab(self.tableWidget, "List")
        grid.addWidget(tabwidget, 0, 0)
    def createTable(self):
        self.tableWidget = QTableWidget()

        # Row count
        self.tableWidget.setRowCount(4)

        # Column count
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setItem(0, 0, QTableWidgetItem("Command"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Path/URL"))
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
def button_click(a,b):
    # shost is a QString object
    cmndtxt = a
    pathtxt=b
    print(cmndtxt)
    print (pathtxt)
    if db.is_connected():
        print("connected")
        cur = db.cursor()
        sql="INSERT INTO Commands (ip,command,path) VALUES(%s,%s,%s)"
        val = (haship,cmndtxt, pathtxt)
        cur.execute(sql,val)
        db.commit()

# logo widget
image = QPixmap("microphone.png")
button = QPushButton()
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
button.clicked.connect(start)
grid.addWidget(button, 4, 0, 1, 2)

def scndintrfc():

    screen = Window()
    window.setLayout(grid)
    window.show()



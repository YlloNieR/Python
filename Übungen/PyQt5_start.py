import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QIcon,QFont
from PyQt5 import QtCore

class Fenster(QWidget):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        QToolTip.setFont(QFont('Arial',14))
        bDO = QPushButton('Drück mich ganz fest', self)
        bEnde = QPushButton('Ende', self)
        bDO.move(450,150) 
        bEnde.move(450,250)    
        bDO.setToolTip('this is my <b>Button<b/>')
        bDO.clicked.connect(self.gedrueckt)
        bEnde.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.setToolTip("das ist ein Fenster")
        self.setGeometry(350, 150, 1000, 500)
        self.setWindowTitle("asd")
        self.show()        
    
    def gedrueckt(self):
        print("alles ready")

    def ende(self):
        print("alles ready")





app = QApplication(sys.argv)
w = Fenster()

sys.exit(app.exec_())
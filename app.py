import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFrame
from PyQt5.QtGui import QIcon

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        
        #==============WINDOW PROPERTIES==============
        self.title = 'Image Compressor by Mert' # window title
        self.left = 10
        self.top = 10
        self.width = 400 # setting window size to 400x600
        self.height = 600
        self.setFixedSize(self.width, self.height) # disable window expanding
        self.setObjectName("main_window") # create object
        stylesheet = ""
        with open("design.qss", "r") as f:
            stylesheet = f.read()
        self.setStyleSheet(stylesheet) # importing design.qss as stylesheet
        # self.setStyleSheet("background-color:black") # change background color to black
        self.initUI()
        #=============================================
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #=================MAIN WINDOW=================

        self.single_bubble = QFrame(self) # create 1. frame named single_bubble
        self.single_bubble.setObjectName("bubble") # connect with qss
        self.single_bubble.move(50, 100) # locate
        self.single_bubble.mousePressEvent = self.single_bubble_clicked # click event

        self.dir_bubble = QFrame(self) # create 2. frame named dir_bubble
        self.dir_bubble.setObjectName("bubble") # connect with qss
        self.dir_bubble.move(50, 275) # locate
        self.dir_bubble.mousePressEvent = self.dir_bubble_clicked # click event

        #=============================================

        self.show()
    
    #==================================FUNCTIONS==================================

    def single_bubble_clicked(self, event):
        print("single bubble clicked")
        print(event)

    def dir_bubble_clicked(self, event):
        print("dir bubble clicked")
        print(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
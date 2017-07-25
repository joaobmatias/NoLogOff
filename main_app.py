import pyautogui
import sys
from PyQt4 import QtGui, QtCore

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 10


class App_Window(QtGui.QWidget):
    def __init__(self):
        super(App_Window, self).__init__()

        self.initUI()

    def initUI(self):
        btn = QtGui.QPushButton('Start moving the mouse', self)
        btn.clicked.connect(self.moveMouse)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        btn2 = QtGui.QPushButton('Stop and Quit program', self)
        quit = btn2.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn2.size()
        btn2.move(51, 100)

        self.center()
        self.resize(300, 150)
        self.setWindowTitle('NoLogOff')
        self.show()


    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def moveMouse(self, btn2):

        while btn2.clicked.connect() != True:
            pyautogui.moveRel(100, 0, duration=0.25)
            pyautogui.moveRel(0, 100, duration=0.25)
            pyautogui.moveRel(-100, 0, duration=0.25)
            pyautogui.moveRel(0, -100, duration=0.25)




def main():
    app = QtGui.QApplication(sys.argv)
    ex = App_Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'pyqt5tests.ui'
# Created by: PyQt5 UI code generator 5.9.2
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import time

ser = serial.Serial('/dev/ttyUSB1', baudrate = 115200, timeout = 0.5)

time.sleep(0.5)

# ========================================================================================
# ----------------------------------------------------------------------------------------
class Ui_MainWindow(object):

    # ------------------------------------------------------------------------------------
    def setup_Ui(self, MainWindow): # GUI
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 540, 32))
        self.label.setObjectName("label")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 70, 520, 300))
        self.textEdit.setObjectName("textEdit")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 410, 520, 32))
        self.pushButton.setObjectName("pushButton")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.menubar.setObjectName("menubar")
        
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)

        self.retranslate_Ui(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # ------------------------------------------------------------------------------------
    def retranslate_Ui(self, MainWindow): # 재번역 UI
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UART Terminal v1.0")) # window title name

        self.label.setText(_translate("MainWindow", "PyQT5..!!!")) # label에 처음에 표시되는 글자
        self.pushButton.setText(_translate("MainWindow", "Button"))
        self.pushButton.clicked.connect(self.label_change_UI) # 버튼 누르면 글자바뀜
        
        self.thread_start = MyThread()
        self.thread_start.ard_signal.connect(self.label.setText)    # label text signal
        self.thread_start.but_signal.connect(self.textEdit.setText) # textEdit text signal / couunter
        self.thread_start.thr_signal.connect(self.textEdit.setText) # textEdit text signal / couunter
        self.thread_start.start()
        
    # ------------------------------------------------------------------------------------
    def label_change_UI(self): # 버튼을 누르면 editText와 Button 글자가 바뀜
        self.pushButton.setText('Button Clicked!')
        self.textEdit.setText('Hello, World!!!')
    
    # ------------------------------------------------------------------------------------
    def print_UI(self, message):
        self.textEdit.setText(message)

# ----------------------------------------------------------------------------------------
class MyThread(QtCore.QThread):
    ard_signal = QtCore.pyqtSignal(str)
    but_signal = QtCore.pyqtSignal(str)
    thr_signal = QtCore.pyqtSignal(str)
    
    def __init__(self):
        QtCore.QThread.__init__(self)
        
    def run(self):
        counter = 0
        while 1:
            time.sleep(0.5)
            self.ard_signal.emit(str(ser.readline().decode().split('\r\n')[0]))
            counter += 1
            self.but_signal.emit("Counter :"+str(counter))
            print("Counter :", counter)
        sys.exit()

# ========================================================================================
if __name__ == "__main__": # main 함수, window 뜨게 하는 곳
#-----------------------------------------------------------------------------------------
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setup_Ui(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())


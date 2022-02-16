from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import serial
import time
import sys
from PyQt5 import QtCore, QtWidgets

ser = serial.Serial('/dev/ttyUSB1', baudrate = 115200, timeout = 0.5)

time.sleep(0.5)

#-------------------------------------------------------------------------------
class MyApp(QWidget):
#-------------------------------------------------------------------------------
    def __init__(self):
        super().__init__()
        self.initUI()
        global flag_open # 직렬 포트가 열려 있는지 여부를 결정하는 플래그 비트
        self.flag_open = 0

    #---------------------------------------------------------------------------
    def initUI(self):
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.set_timer)
        
        self.label1 = QLabel(QTime.currentTime().toString('hh:mm:ss'), self)

        self.edit1 = QLineEdit('센서 값', self)
        self.btn = QPushButton('버튼', self)

        self.time_thread_start = timeThread()
        self.btn.clicked.connect(self.btn_clicked)
        self.time_thread_start.start()

        grid = QGridLayout()
        grid.addWidget(self.label1, 0, 0)
        grid.addWidget(self.edit1, 0, 1)
        grid.addWidget(self.btn, 0, 3)

        self.setLayout(grid)
        self.setWindowTitle('My First Application')
        self.move(500, 300)
        self.resize(700, 700)
        self.show()

    #---------------------------------------------------------------------------
    def set_timer(self):

        self.label1.setText(QTime.currentTime().toString('hh:mm:ss'))

    #---------------------------------------------------------------------------
    def btn_clicked(self):
        while True:
            self.message=ser.readline()
            print(self.message)

#-------------------------------------------------------------------------------
class signalThread(QtCore.QThread):
#-------------------------------------------------------------------------------
    signal = QtCore.pyqtSignal(str)

    def __init__(self, parent): #parent는 WindowClass에서 전달하는 self이다.(WidnowClass의 인스턴스) 
        super().__init__(parent) 
        self.parent = parent #self.parent를 사용하여 WindowClass 위젯을 제어할 수 있다. 
         
    def run(self): #쓰레드로 동작시킬 함수 내용 구현
        while 1:
            time.sleep(0.5)
            self.signal.emit(str(ser.readline().decode().split('\r\n')[0]))
        sys.exit()

#-------------------------------------------------------------------------------
class timeThread(QtCore.QThread):
#-------------------------------------------------------------------------------
    signal = QtCore.pyqtSignal(str)

    def run(self): #쓰레드로 동작시킬 함수 내용 구현
        ex.label1.setText(QTime.currentTime().toString('hh:mm:ss'))

#-------------------------------------------------------------------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
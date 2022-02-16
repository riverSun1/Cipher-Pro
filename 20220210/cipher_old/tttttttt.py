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

    #---------------------------------------------------------------------------
    def initUI(self):
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.set_timer)
        
        self.label1 = QLabel(QTime.currentTime().toString('hh:mm:ss'), self)
        self.edit1 = QLineEdit('센서 값', self)
        self.btn = QPushButton('버튼', self)

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

    # ------------------------------------------------------------------------------------
    def re_ui(self, MainWindow):
        self.thread_start = Thread()
        self.thread_start.signal.connect(self.edit1.setText) # textEdit text signal
        self.thread_start.start()

#-------------------------------------------------------------------------------
class Thread(QtCore.QThread): #초기화 메서드 구현 
#-------------------------------------------------------------------------------
    signal = QtCore.pyqtSignal(str)

    def __init__(self, parent): #parent는 WndowClass에서 전달하는 self이다.(WidnowClass의 인스턴스) 
        super().__init__(parent) 
        self.parent = parent #self.parent를 사용하여 WindowClass 위젯을 제어할 수 있다. 
         
    def run(self): #쓰레드로 동작시킬 함수 내용 구현
        while 1:
            time.sleep(0.5)
            self.signal.emit(str(ser.readline().decode().split('\r\n')[0]))
        sys.exit()

#-------------------------------------------------------------------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
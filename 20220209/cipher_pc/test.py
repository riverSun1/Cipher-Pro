import sys
from PyQt5.QtWidgets import QApplication, QWidget
from cipher import MyApp
import cipher as c
import time
import serial
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout

ser = serial.Serial(
    port = "/dev/ttyUSB1",
    baudrate = 115200,
    bytesize = serial.EIGHTBITS, 
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE, 
    timeout = 0.5,
    xonxoff = True,
    rtscts = False,
    dsrdtr = False,
    writeTimeout = 0.5
    )

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        edit = QLineEdit('abc')
        vbox.addWidget(edit)
        self.setLayout(vbox)

        self.setWindowTitle('My First Application')
        self.move(300, 300)
        self.resize(400, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    edit = QLineEdit()

    check_flag = ser.isOpen()
    print("Polling Comm port Check :", check_flag, "\n")

    while check_flag :
        if ser.readable(): 
            res = ser.readline() 
            edit.setText(res.decode()[:len(res) - 2])

    ser.close()

    sys.exit(app.exec_())
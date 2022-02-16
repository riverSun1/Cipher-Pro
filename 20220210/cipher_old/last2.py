import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, \
                            QGridLayout, QLabel, QMessageBox
import serial
import time
import serial.tools.list_ports

#-----------------------------------------------------------------------------------------
class MyApp(QWidget):
#-----------------------------------------------------------------------------------------
    def __init__(self):
        super(MyApp, self).__init__()
        self.initUI()
        global flag_open # 직렬 포트가 열려 있는지 여부를 결정하는 플래그 비트 # 전역 변수
        self.flag_open = 0 # port가 닫힌 상태

    #-------------------------------------------------------------------------------------
    def initUI(self): # window layout
        grid = QGridLayout()

        self.portname = QLabel("Port number")
        self.datanumber = QLabel("Send data bits:")
        self.datasender = QLabel("Send data:")
        self.datareview = QLabel("Receiving data:")

        self.button = QPushButton("Send out")
        self.open_button = QPushButton("open")

        self.portnameEdit = QLineEdit()
        self.datanumberEdit = QLineEdit()
        self.datasenderEdit = QLineEdit()
        self.datareviewEdit = QLineEdit()

        grid.addWidget(self.portname, 1, 0)
        grid.addWidget(self.portnameEdit, 1, 1)
        grid.addWidget(self.datanumber, 2, 0)
        grid.addWidget(self.datanumberEdit, 2, 1)

        grid.addWidget(self.datasender, 3, 0,)
        grid.addWidget(self.datasenderEdit, 3, 1, 1, 6)
        grid.addWidget(self.datareview, 4, 0)
        grid.addWidget(self.datareviewEdit, 4, 1, 1, 6)
        
        grid.addWidget(self.button, 5, 3)
        grid.addWidget(self.open_button, 5, 1)
        self.setLayout(grid)

        self.button.clicked.connect(self.cosender)
        self.open_button.clicked.connect(self.check_serial)

        self.setGeometry(300,300,200,200)
        self.setWindowTitle("serial monitor")

    #-------------------------------------------------------------------------------------    
    def messageUI(self):
        '''Tips'''
        QMessageBox.critical(self, " ", "직렬 포트를 열지 못했습니다. 올바른 직렬 포트를 선택하십시오.")

    #-------------------------------------------------------------------------------------
    def check_serial(self):
        '''직렬 포트가 열려 있는지 감지'''
        try:
            self.t = serial.Serial('/dev/ttyUSB1', 115200) # open Serial Port
            port = self.t.portstr # Return but port number
            self.portnameEdit.setText(port) # Display on the interface
            self.flag_open=1

        except serial.serialutil.SerialException: #Failed to open, output prompt information
            self.messageUI() #Tips

    #-------------------------------------------------------------------------------------
    def cosender(self):
        if self.flag_open==1:
            if self.flag_open == 1:  # Serial port is opened
                self.str_input = self.datasenderEdit.text()  # Return the sending text above
                n = self.t.write((self.str_input + '\n').encode())
                self.datanumberEdit.setText(str(n - 1))  # Write data digit box
                self.datasenderEdit.setText(str(self.str_input))  # Write to send box
                time.sleep(1)  # sleep() and inWaiting() are best used in pairs
                num = self.t.inWaiting()  # Get the length of the received data

                if num:
                    self.receivemessage = self.t.read(num)  # Read and receive data
                    print(self.receivemessage)
                    self.datareviewEdit.setText(str(self.receivemessage)[2:-3])  # Write to receive box
        else:
            self.messageUI()

#-----------------------------------------------------------------------------------------
if __name__ == "__main__":
#-----------------------------------------------------------------------------------------
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
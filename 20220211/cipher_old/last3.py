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
        self.datareview = QLabel("Receiving data:")

        self.button = QPushButton("Send out")
        self.open_button = QPushButton("open")

        self.portnameEdit = QLineEdit()
        self.datareviewEdit = QLineEdit()

        grid.addWidget(self.portname, 1, 0)
        grid.addWidget(self.portnameEdit, 1, 1, 1, 6)

        grid.addWidget(self.datareview, 4, 0)
        grid.addWidget(self.datareviewEdit, 4, 1, 1, 6)

        grid.addWidget(self.button, 5, 3) # send out 버튼
        grid.addWidget(self.open_button, 5, 1) # open 버튼

        self.setLayout(grid)

        self.button.clicked.connect(self.cosender)
        self.open_button.clicked.connect(self.check_serial) # open 버튼을 누르면 포트를 찾아주는 함수로 이동

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
            self.portnameEdit.setText(port) # Display on the interface # 포트를 알아서 찾아서 editText에 나타냄
            self.flag_open=1 # 포트가 열렸다.

        except serial.serialutil.SerialException: # Failed to open, output prompt information # 포트가 안 열렸을때 예외처리
            self.messageUI() #Tips

    #-------------------------------------------------------------------------------------
    def cosender(self):
        if self.flag_open==1: # 포트가 열렸다면

            while self.flag_open :

                self.message=self.t.readline()
                print(self.message)
                self.datareviewEdit.setText(str(self.message)[2:-3])

                self.t.close()
                self.t = serial.Serial('/dev/ttyUSB1', 115200)

        else: # Tips
            self.messageUI()

#-----------------------------------------------------------------------------------------
if __name__ == "__main__":
#-----------------------------------------------------------------------------------------
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
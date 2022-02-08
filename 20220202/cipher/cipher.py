import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QGridLayout
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QGroupBox
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QPixmap
import qdarkstyle #다크테마

#-----------------------------------------------------------------------------------------
class MyApp(QWidget):
#-----------------------------------------------------------------------------------------

    def __init__(self):
        super().__init__()
        self.initUI()

    #-------------------------------------------------------------------------------------

    def initUI(self):

        grid = QGridLayout()
        vbox = QVBoxLayout()
        pixmap = QPixmap('./main_img.jpg')
        lbl_img = QLabel()
        self.edit4 = QLineEdit()
        self.edit5 = QLineEdit()

        lbl_img.setPixmap(pixmap)
        grid.addWidget(self.createPlainTextGroup(), 0, 0)
        grid.addWidget(self.createCipherTextGroup(), 0, 1)

        vbox.addWidget(lbl_img)
        vbox.addLayout(grid)
        vbox.addWidget(self.createSensorGroup())

        self.setStyleSheet( "padding: 10px;"
                            "margin-top: 7px;"
                            "margin-bottom: 7px;"
                            "margin-left: 5px;"
                            "margin-right: 5px;"
                            "font-size: 16pt;")

        self.setLayout(vbox)
        self.setWindowTitle('Cipher Pro')
        #self.resize(1000, 300)
        self.setFixedSize(1000, 950)
        self.center() #center() 메서드를 통해서 창이 화면의 가운데에 위치
        self.show()
        
    #-------------------------------------------------------------------------------------

    def id_btn_clicked(self):
        #self.edit1.setText('버튼먹히는지 확인용')
        #self.edit4.setText(self.enc_xor(edit1., key))

        #text = self.edit1.text() # line_edit text 값 가져오기
        #self.edit4.setText(text)

        plaintext = self.edit1.text()
        key = self.edit3.text()
        ciphertext = self.enc_xor(plaintext, key)
        self.edit4.setText(ciphertext)

    #-------------------------------------------------------------------------------------

    def time_btn_clicked(self):
        
        plaintext = self.edit1.text()
        key = self.edit3.text()
        ciphertext = self.enc_xor(plaintext, key)
        self.edit4.setText(ciphertext)

    #-------------------------------------------------------------------------------------

    def sen_btn_clicked(self):
        
        self.edit2.setText(QTime.currentTime().toString('hh:mm:ss'))

    #-------------------------------------------------------------------------------------

    def enc_xor(self, msg, key): # 두 값 비교해서 같으면 0, 다르면 1
        msg_size = len(msg)
        key_size = len(key)
        enc = bytearray() # 빈 바이트 배열 객체 생성

        for i in range(msg_size):
            msg_xor = ord(msg[i]) ^ ord(key[i%key_size])
            enc.append(msg_xor)
        #print(enc)
        #print(str(enc))
        #print(enc.decode())

        return str(enc)

    #-------------------------------------------------------------------------------------

    def createPlainTextGroup(self):
        groupbox = QGroupBox('Key Plaintext')

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.set_timer)

        label1 = QLabel('고유ID', self)
        label2 = QLabel('시간', self)
        label3 = QLabel('생산자', self)

        self.edit1 = QLineEdit('unique id', self)
        self.edit2 = QLineEdit(QTime.currentTime().toString('hh:mm:ss'), self)
        self.edit3 = QLineEdit('haewon', self)

        Btn1 = QPushButton("Convert")
        Btn2 = QPushButton("Convert")

        Btn1.clicked.connect(self.id_btn_clicked)
        Btn2.clicked.connect(self.time_btn_clicked)

        grid1 = QGridLayout()
        grid1.addWidget(label1, 0, 0)
        grid1.addWidget(label2, 1, 0)
        grid1.addWidget(label3, 2, 0)
        grid1.addWidget(self.edit1, 0, 1)
        grid1.addWidget(self.edit2, 1, 1)
        grid1.addWidget(self.edit3, 2, 1)
        grid1.addWidget(Btn1,0,2)
        grid1.addWidget(Btn2,1,2)

        groupbox.setLayout(grid1)

        return groupbox

    #-------------------------------------------------------------------------------------

    def set_timer(self):
        self.edit2.setText(QTime.currentTime().toString('hh:mm:ss'))

    #-------------------------------------------------------------------------------------

    def createCipherTextGroup(self):
        groupbox = QGroupBox('Key Ciphertext')

        label4 = QLabel('고유ID', self)
        label5 = QLabel('시간', self)
        label6 = QLabel('생산자', self)

        #edit4 = QLineEdit()
        #edit5 = QLineEdit()
        edit6 = QLineEdit('haewon')

        grid2 = QGridLayout()
        grid2.addWidget(label4, 0, 0)
        grid2.addWidget(label5, 1, 0)
        grid2.addWidget(label6, 2, 0)
        grid2.addWidget(self.edit4, 0, 1)
        grid2.addWidget(self.edit5, 1, 1)
        grid2.addWidget(edit6, 2, 1)

        groupbox.setLayout(grid2)

        return groupbox

    #-------------------------------------------------------------------------------------

    def createSensorGroup(self):
        groupbox = QGroupBox('Sensor')

        label1 = QLabel('암호화된 센서 값', self)
        label2 = QLabel('복호화된 센서 값', self)

        edit2 = QLineEdit()
        edit3 = QLineEdit()

        Btn3 = QPushButton("Convert")
        Btn3.clicked.connect(self.sen_btn_clicked)

        grid3 = QGridLayout()
        grid3.addWidget(label1, 0, 0)
        grid3.addWidget(label2, 1, 0)
        grid3.addWidget(edit2, 0, 1)
        grid3.addWidget(edit3, 1, 1)
        grid3.addWidget(Btn3,0,2)

        groupbox.setLayout(grid3)

        return groupbox

    #-------------------------------------------------------------------------------------

    def center(self):
        qr = self.frameGeometry() #창의 위치와 크기 정보를 가져옵니다.
        cp = QDesktopWidget().availableGeometry().center() #사용하는 모니터 화면의 가운데 위치를 파악합니다.
        qr.moveCenter(cp) #창의 직사각형 위치를 화면의 중심의 위치로 이동
        self.move(qr.topLeft()) #현재 창을, 화면의 중심으로 이동했던 직사각형(qr)의 위치로 이동

#-----------------------------------------------------------------------------------------
if __name__ == '__main__': # 모듈의 이름이 저장되는 내장 변수
#-----------------------------------------------------------------------------------------

    app = QApplication(sys.argv) #모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야 합니다.
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5')) #다크테마
    ex = MyApp()
    sys.exit(app.exec_())

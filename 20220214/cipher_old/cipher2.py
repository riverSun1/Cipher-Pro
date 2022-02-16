import sys
import binascii
import serial
import qdarkstyle

from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication, QLabel, QLineEdit, \
    QPushButton, QVBoxLayout, QGroupBox
from PyQt5.QtCore import QTimer, QTime, QCoreApplication, Qt, QThread, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtWidgets

rc=''
i=0

ser = serial.Serial('/dev/ttyUSB1', baudrate = 115200, timeout = 0.5)

#timer = QTimer()
#timer.start(1000)

views = 0

#---------------------------------------------------------------------------------
class TestThread(QThread): # 스레드
#---------------------------------------------------------------------------------
	serialUpdate = pyqtSignal(str) # signal이 발생하면

	#-----------------------------------------------------------------------------
	def run(self):
		while ser.is_open:
			QThread.sleep(1)			
			value = ser.readline().decode()
			self.serialUpdate.emit(value) # esp로부터 들어온 값을 serialUpdate로 보낸다.
			# pyqt는 사용자가 정의한 signal을 발생(emit)할 수 있다. 
			# emit시 signal에 연결(connect)된 slot을 호출하게 된다.
			ser.flush() # 버퍼 비우기

#-----------------------------------------------------------------------------------------
class MyApp(QWidget):
#-----------------------------------------------------------------------------------------
    title = []

    def __init__(self):
        super().__init__()

        self.thread = TestThread(self)
        self.thread.serialUpdate.connect(self.handleSerialUpdate)
        self.thread.start()
        
        self.initUI()
        MyApp.title = 'PC'
        
        global views
        
        if views == 0:
            MyApp.title = 'PC'
        else:
            MyApp.title = 'IoT'
        #print("MyApp.title", MyApp.title)

    #-------------------------------------------------------------------------------------
    def initUI(self):

        grid = QGridLayout()
        vbox = QVBoxLayout()
        pixmap = QPixmap('./main_img.jpg')
        lbl_img = QLabel()

        #self.timer = QTimer(self)
        #self.timer.start(1000)
        
        if views == 0: # 0 = PC, 1 = IoT
            self.edit1 = QLineEdit('unique id', self)
            self.edit2 = QLineEdit(QTime.currentTime().toString('hhmmss'), self)
            self.edit3 = QLineEdit('haewon', self)
            self.edit3.textChanged.connect(self.lineEditChanged)

        self.edit4 = QLineEdit()
        self.edit5 = QLineEdit()
        self.edit6 = QLineEdit()

        self.edit7 = QLineEdit('sensor value') # 아두이노로부터 읽어들인 센서값
        self.edit8 = QLineEdit() # key값 표시
        self.edit9 = QLineEdit() # 암호화된 센서값 표시
        self.edit10 = QLineEdit() # 복호화된 센서값 표시
        
        Qbtn = QPushButton('Quit', self)
        Qbtn.resize(Qbtn.sizeHint())
        #Qbtn.setMaximumHeight(500)
        #Qbtn.setMaximumWidth(500)
        Qbtn.clicked.connect(QCoreApplication.instance().quit)

        self.sen_enc_btn1 = QPushButton("encryption")
        self.sen_enc_btn1.clicked.connect(self.sen_enc_xor)

        lbl_img.setPixmap(pixmap)
        grid.addWidget(self.createPlainTextGroup(), 0, 0)
        grid.addWidget(self.createCipherTextGroup(), 0, 1)

        vbox.addWidget(lbl_img)
        vbox.addLayout(grid)
        vbox.addWidget(self.createSensorGroup())
        vbox.addWidget(Qbtn, alignment=Qt.AlignRight)
        
        Qbtn.setStyleSheet( "background-color:#F44336;")

        self.setStyleSheet( "padding: 10px;"
                            "margin-top: 7px;"
                            "margin-bottom: 7px;"
                            "margin-left: 5px;"
                            "margin-right: 5px;"
                            "font-size: 12pt;")

        self.setLayout(vbox)
        #self.setWindowTitle('Cipher Pro')
        self.setFixedSize(1000, 1200)
        #self.center() #center() 메서드를 통해서 창이 화면의 가운데에 위치
        self.show()
        
    #-------------------------------------------------------------------------------------
    def change_title(self, title):
        #if MyApp.title is title1:
        #    print("test", title1)

        #if title1 is not None:
        #    MyApp.title = title1
        self.setWindowTitle(MyApp.title)

    #-------------------------------------------------------------------------------------
    def id_btn_clicked(self):
        #self.edit1.setText('함수 호출 확인용')
        #text = self.edit1.text() # line_edit text 값 가져오기
        #self.edit4.setText(text)

        plaintext = self.edit1.text()
        key = self.edit3.text()
        ciphertext = self.enc_xor(plaintext, key)
        self.edit4.setText(ciphertext)

    #-------------------------------------------------------------------------------------
    def time_btn_clicked(self):

        self.time_btn_clicked_2()

    #-------------------------------------------------------------------------------------
    def time_btn_clicked_2(self):

        #self.timer = QTimer(self)
        #self.timer.start(1000)
        self.timer.timeout.connect(self.time_enc_xor)

    #-------------------------------------------------------------------------------------
    #def sen_enc_btn_clicked(self):
        
    #    self.sen_enc_btn_clicked_2()

    #-------------------------------------------------------------------------------------
    #def sen_enc_btn_clicked_2(self):
        
    #    self.timer.timeout.connect(self.sen_enc_xor)

    #-------------------------------------------------------------------------------------
    def sen_dec_btn_clicked(self):
        
        self.timer.timeout.connect(self.sen_dec_btn_clicked_2)

    #-------------------------------------------------------------------------------------
    def sen_dec_btn_clicked_2(self):
        
        self.timer.timeout.connect(self.sen_dec_xor)

    #-------------------------------------------------------------------------------------
    def lineEditChanged(self):
        self.edit6.setText(self.edit3.text())

    #-------------------------------------------------------------------------------------
    def enc_xor(self, msg, key): # 암호화 # 두 값 비교해서 같으면 0, 다르면 1
        msg_size = len(msg)
        key_size = len(key)
        enc = bytearray() # 빈 바이트 배열 객체 생성

        for i in range(msg_size): # 문자를 xor하는 것은 불가능하기 때문에 숫자로 바꿔줘야 한다. -> ord()
            msg_xor = ord(msg[i]) ^ ord(key[i % key_size]) # ord() - 해당 문자에 해당하는 유니코드 정수를 반환
            enc.append(msg_xor)
        #print(enc)
        #print(str(enc))
        #print(enc.decode())
        
        #return str(enc) # string type으로 변환
        return str(binascii.hexlify(enc), "utf-8") # string type으로 변환 # binascii.hexlify() - 이진 데이터의 16 진수 표현을 반환

    #-------------------------------------------------------------------------------------
    def dec_xor(self, cipher_msg, key): # 복호화 # 두 값 비교해서 같으면 0, 다르면 1
        msg_size = len(cipher_msg)
        key_size = len(key)
        enc = bytearray() # 빈 바이트 배열 객체 생성

        for i in range(msg_size): # 문자를 xor하는 것은 불가능하기 때문에 숫자로 바꿔줘야 한다. -> ord()
            msg_xor = ord(cipher_msg[i]) ^ ord(key[i % key_size]) # ord() - 해당 문자에 해당하는 유니코드 정수를 반환
            enc.append(msg_xor)
 
        #return enc
        #return str(enc)
        return str(enc.decode())
        #return enc.decode()
        #return str(binascii.unhexlify(enc), "utf-8")

    #-------------------------------------------------------------------------------------
    def time_enc_xor(self):

        plaintext = self.edit2.text()
        key = self.edit3.text()

        self.edit3.textChanged.connect(self.lineEditChanged)

        ciphertext = self.enc_xor(plaintext, key)
        self.edit5.setText(ciphertext)
        self.edit8.setText(ciphertext)

    #-------------------------------------------------------------------------------------
    def sen_enc_xor(self): # 센서 값 암호화

        # 암호화된 고유ID + 시간을 key 값으로 받아온다.
        cip_id = self.edit4.text()

        plaintext = self.edit2.text()
        key = self.edit3.text()
        cip_time = self.enc_xor(plaintext, key)

        key = cip_id + cip_time
        self.edit8.setText(key)

        ciphertext = self.enc_xor(plaintext, key)
        self.edit9.setText(ciphertext)

        #---------------------------------------------------------------------------------
        #time_plaintext = self.edit2.text()
        #time_key = self.edit3.text()
        #sensor_plaintext = self.edit7.text()

        #key = self.enc_xor(time_plaintext, time_key)

        #self.edit8.setText(key)

        #enc_sensor = self.enc_xor(sensor_plaintext, key)

        #self.edit9.setText(enc_sensor)

    #-------------------------------------------------------------------------------------
    def sen_dec_xor(self): # 센서 값 복호화

        # 고유 ID
        cip_id = self.edit4.text()

        # 시간 값 암호화
        plaintext = self.edit2.text()
        key = self.edit3.text()
        cip_time = self.enc_xor(plaintext, key)

        # 센서 값을 암호화하기 위한 key값 (암호화된 고유id값 + 시간값)
        key = cip_id + cip_time

        # 센서 값 암호화
        ciphertext = self.enc_xor(plaintext, key)

        # 센서 값을 암호화 한것을 다시 복호화
        plaintext = self.dec_xor(ciphertext, key)
        self.edit10.setText(plaintext)
        #---------------------------------------------------------------------------------
        #time_plaintext = self.edit2.text()
        #time_key = self.edit3.text()
        #sensor_plaintext = self.edit7.text()

        #key = self.enc_xor(time_plaintext, time_key)

        #enc_sensor = self.enc_xor(sensor_plaintext, key)

        #dec_sensor = self.dec_xor(enc_sensor, key)

        #self.edit10.setText(dec_sensor.decode())
        
    #-------------------------------------------------------------------------------------
    def createPlainTextGroup(self):
        if views == 0: # 0 = PC, 1 = IoT
        
            groupbox = QGroupBox('Key Plaintext')

            self.timer = QTimer(self)
            self.timer.start(1000)
            self.timer.timeout.connect(self.set_timer)

            label1 = QLabel('고유ID', self)
            label2 = QLabel('시간', self)
            label3 = QLabel('생산자', self)

            grid1 = QGridLayout()
            grid1.addWidget(label1, 0, 0)
            grid1.addWidget(label2, 1, 0)
            grid1.addWidget(label3, 2, 0)
            grid1.addWidget(self.edit1, 0, 1)
            grid1.addWidget(self.edit2, 1, 1)
            grid1.addWidget(self.edit3, 2, 1)

            Btn1 = QPushButton("→")
            Btn2 = QPushButton("→")
            Btn1.clicked.connect(self.id_btn_clicked)
            Btn2.clicked.connect(self.time_btn_clicked)
            #grid1 = QGridLayout()
            grid1.addWidget(Btn1,0,2)
            grid1.addWidget(Btn2,1,2)
        
            groupbox.setLayout(grid1)

            return groupbox

    #-------------------------------------------------------------------------------------
    def set_timer(self):
        self.edit2.setText(QTime.currentTime().toString('hhmmss'))

    #-------------------------------------------------------------------------------------
    def createCipherTextGroup(self):
        if views == 0: # 0 = PC, 1 = IoT
            groupbox = QGroupBox('Key Ciphertext')

            label4 = QLabel('고유ID', self)
            label5 = QLabel('시간', self)
            label6 = QLabel('생산자', self)

            edit = self.edit3.text()
            self.edit6.setText(edit)

            grid2 = QGridLayout()
            grid2.addWidget(label4, 0, 0)
            grid2.addWidget(label5, 1, 0)
            grid2.addWidget(label6, 2, 0)
            grid2.addWidget(self.edit4, 0, 1)
            grid2.addWidget(self.edit5, 1, 1)
            grid2.addWidget(self.edit6, 2, 1)

            groupbox.setLayout(grid2)

            return groupbox

    #-------------------------------------------------------------------------------------
    def createSensorGroup(self):
        groupbox = QGroupBox('Sensor')

        label1 = QLabel('읽어들인 센서 값', self)
        label2 = QLabel('key 값', self)
        label3 = QLabel('암호화된 센서 값', self)
        label4 = QLabel('복호화된 센서 값', self)

        #sen_enc_btn1 = QPushButton("encryption")
        #sen_enc_btn1.clicked.connect(self.sen_enc_btn_clicked)
        sen_enc_btn2 = QPushButton("decryption")
        sen_enc_btn2.clicked.connect(self.sen_dec_btn_clicked)

        grid3 = QGridLayout()
        grid3.addWidget(label1, 0, 0)
        grid3.addWidget(label2, 1, 0)
        grid3.addWidget(label3, 2, 0)
        grid3.addWidget(label4, 3, 0)
        grid3.addWidget(self.edit7, 0, 1)
        grid3.addWidget(self.edit8, 1, 1)
        grid3.addWidget(self.edit9, 2, 1)
        grid3.addWidget(self.edit10, 3, 1)
        grid3.addWidget(self.sen_enc_btn1,0,2)
        grid3.addWidget(sen_enc_btn2,2,2)

        groupbox.setLayout(grid3)

        return groupbox
    
    #-------------------------------------------------------------------------------------
    def handleSerialUpdate(self, value):
        if value != '':
            current_time = QTime.currentTime()
            label_time = current_time.toString('hh:mm:ss > ') # converting QTime object to string
            global rc, i
            rc = rc  + label_time + value # data receive
            
            i = rc.count('\n') # 라인 갯수를 센다. 
            if i > 0: # 라인 갯수가 1이면 리셋
                i = 0
                rc = label_time + value + '\n'

            self.edit7.setText(rc)

#-----------------------------------------------------------------------------------------
if __name__ == '__main__': # 모듈의 이름이 저장되는 내장 변수
#-----------------------------------------------------------------------------------------
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    
    views = 0
    pc = MyApp() # PC
    MyApp.title = 'PC'
    pc.change_title('PC')
    pc.move(250, 100)

    views = 1
    iot = MyApp() # iot
    MyApp.title = 'IoT'
    iot.change_title('IoT')
    iot.move(1300, 100)
    iot.setFixedSize(1000, 900)

    sys.exit(app.exec_())
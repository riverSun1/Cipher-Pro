from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QComboBox
from PyQt5.QtCore import QSize, QRect , QTimer, QTime, Qt, QThread, pyqtSignal
import sys
import serial
import serial.tools.list_ports

rc=''
i=0

ser = serial.Serial('/dev/ttyUSB1', baudrate = 115200, timeout = 1)

#---------------------------------------------------------------------------------
class TestThread(QThread):
#---------------------------------------------------------------------------------
	serialUpdate = pyqtSignal(str) # signal이 발생하면

	#-----------------------------------------------------------------------------
	def run(self):
		while ser.is_open:
			QThread.sleep(1)			
			value = ser.readline().decode()
			self.serialUpdate.emit(value)
			# pyqt는 사용자가 정의한 signal을 발생(emit)할 수 있다. 
			# emit시 signal에 연결(connect)된 slot을 호출하게 된다.

			ser.flush() # 버퍼 비우기

#---------------------------------------------------------------------------------
class Window(QMainWindow):
#---------------------------------------------------------------------------------
	def __init__(self):
		super().__init__()

		self.thread = TestThread(self)
		self.thread.serialUpdate.connect(self.handleSerialUpdate)
		self.thread.start()

		# 타이틀 이름
		self.setWindowTitle("Serial Command")
		self.setGeometry(300, 100, 550, 400)

		# UiComponents() 함수 호출
		self.UiComponents()

		# 모든 위젯 보이게
		self.show()

	#-----------------------------------------------------------------------------
	def closeEvent(self, event): # close gui safely
		self.thread.terminate()
		sys.exit(0)

	#-----------------------------------------------------------------------------
	def UiComponents(self): # 위젯을 위한 함수

		# creating a label
		self.label_r = QLabel(self)
		self.label_r.setGeometry(10, 70, 350, 200)
		self.label_r.setWordWrap(True) # creating label multi line
		self.label_r.setStyleSheet("QLabel"
								"{"
								"border : 1px solid black;"
								"background : white;"
								"}")

		self.label_r.setAlignment(Qt.AlignLeft) # setting alignment to the label
		
        # clear button
		push_clear = QPushButton("Clear", self)
		push_clear.setGeometry(380, 310, 145, 40)
		push_clear.clicked.connect(self.clearData)

	#-----------------------------------------------------------------------------
	def clearData(self):
		global rc, i
		rc=''
		i=0
		self.label_r.setText(rc)

	#-----------------------------------------------------------------------------
	def handleSerialUpdate(self, value):
		if value != '':				
			current_time = QTime.currentTime()
			label_time = current_time.toString('hh:mm:ss:zzz>>') # converting QTime object to string
			
			global rc, i
			rc = rc  + label_time + value # data receive

			i = rc.count('\n') # label_r의 라인 갯수를 센다. 
			if i > 14: # 라인이 15면 리셋
				i = 0
				rc = label_time + value + '\n'
			
			self.label_r.setText(rc)
			self.label_r.setWordWrap(True)

#---------------------------------------------------------------------------------
App = QApplication(sys.argv) # create pyqt5 app
window = Window() # create the instance of our Window
sys.exit(App.exec()) # start the app
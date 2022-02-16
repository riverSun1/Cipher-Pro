import sys 
from cipher import MyApp
import cipher as c
from PyQt5.QtWidgets import QApplication, QWidget
import qdarkstyle
import time
import serial

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

#-----------------------------------------------------------------------------------------
def port_comm():
#-----------------------------------------------------------------------------------------
    
    if ser.readable(): 
        res = ser.readline() 
        #print(res.decode()[:len(res) - 2])
        test = c.edit10
        test.setText(res.decode()[:len(res) - 2])
        #if : exit()

    ser.close()

#-----------------------------------------------------------------------------------------
if __name__ == '__main__': # 모듈의 이름이 저장되는 내장 변수
#-----------------------------------------------------------------------------------------

    app = QApplication(sys.argv) #모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야 합니다.
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5')) #다크테마
    
    c.views = 0
    pc = MyApp() # PC
    MyApp.title = 'PC'
    pc.change_title('PC')
    pc.move(250, 100)

    c.views = 1
    iot = MyApp() # iot
    MyApp.title = 'IoT'
    iot.change_title('IoT')
    iot.move(1300, 100)
    port_comm()

    sys.exit(app.exec_())

    #------------------------------------------------------------------------------------

#    time.sleep(0.5)
#    check_flag = ser.isOpen() #ser.open()
#    print("Polling Comm port Check :", check_flag, "\n")
#    while check_flag :
#        if ser.readable(): 
#            res = ser.readline() 
#            print(res.decode()[:len(res) - 2])
#            #print(res)
#            #if : exit()

    #ser.close()
    #------------------------------------------------------------------------------------

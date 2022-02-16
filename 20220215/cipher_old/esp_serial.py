import time
import serial
import threading

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

if __name__ == '__main__':
    time.sleep(0.5)
    check_flag = ser.isOpen() #ser.open()
    print("Polling Comm port Check :", check_flag, "\n")
    while check_flag :
        if ser.readable(): 
            res = ser.readline() 
            print(res.decode()[:len(res) - 2])
            #print(res)
            #if : exit()

    ser.close()
# ================================================================================
#port = '/dev/ttyUSB0'
#baud = 115200
#ser = serial.Serial(port, baud, timeout=1)

#def main():
#    thread = threading.Thread(target=readthread, args=(ser,))
#    thread.start()

#    #while True:
#    #    data = "보낼데이터(byte형식으로 보내야함 byte,str,encode())"
#    #    ser.write(data)
#    #    time.sleep(1)

#def readthread(ser):
#    while True:
#        if ser.readable():
#            res = ser.readline()
#            print(res)
#    ser.close()

#main()


#-------------------------------------------------------------------------------
#ser = serial.Serial(
#    #port = '/dev/ttyACM0',\
#    port = '/dev/ttyUSB0', baudrate=115200,\
#    parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,\
#    bytesize=serial.EIGHTBITS, timeout=0)

#while True:
#    #commend = input('아두이노에게 내릴 명령:')
#    #py_serial.write(commend.encode())
#    #time.sleep(0.1)
    
#    if ser.readable():
#        # 들어온 값이 있으면 값을 한 줄 읽음 (BYTE 단위로 받은 상태)
#        # BYTE 단위로 받은 response 모습 : b'\xec\x97\x86\xec\x9d\x8c\r\n'
#        response = ser.readline()
#        # 디코딩 후, 출력 (가장 끝의 \n을 없애주기위해 슬라이싱 사용)
#        #print(response[:len(response)-1].decode())
#        print(response.decode())

#-------------------------------------------------------------------------------

'''
print(ser.portstr) #연결된 포트 확인.
ser.write(bytes('hello', encoding='ascii')) #출력방식1
ser.write(b'hello') #출력방식2
ser.write(b'\xff\xfe\xaa') #출력방식3
#출력방식4
vals = [12, 0, 0, 0, 0, 0, 0, 0, 7, 0, 36, 100] 
ser.write(bytearray(vals))
ser.read(ser.inWaiting()) #입력방식1
ser.close()
'''
'''
comport 찾을 때 명령 - lsusb, ls -al

dmesg | grep ttyUSB

ls -l /dev/ttyACM*
ls -l /dev/ttyUSB*

udevadm test $(udevadm info -q path -n /dev/ttyACM0)
udevadm test $(udevadm info -q path -n /dev/ttyUSB0)
'''
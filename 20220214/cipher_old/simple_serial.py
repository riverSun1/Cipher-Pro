import serial
import time
import threading

class SerialPort:
    message=''

    def __init__(self, port, buand):
        super(SerialPort, self).__init__()
        self.port=serial.Serial(port,buand)
        self.port.close()

        if not self.port.isOpen():
            self.port.open()

    def port_open(self):
        if not self.port.isOpen():
            self.port.open()

    def port_close(self):
        self.port.close()

    def send_data(self):
        data = input("???중국어: ")
        n = self.port.write((data+'\n').encode())
        return n
    
    def read_data(self):
        while True:
            self.message=self.port.readline()
            print(self.message)


serialPort="/dev/ttyUSB1"
baudRate=115200

if __name__ == '__main__':

    mSerial=SerialPort(serialPort,baudRate)
    t1=threading.Thread(target=mSerial.read_data)

    t1.start()
    while True:
        time.sleep(1)
        mSerial.send_data()
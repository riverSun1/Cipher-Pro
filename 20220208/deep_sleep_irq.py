import machine
from machine import UART, Pin
from time import sleep

# ------------------------------------------------------------------------------
led = Pin (2, Pin.OUT)
led1 = Pin (19, Pin.OUT)
led2 = Pin (23, Pin.OUT)

interruptCounter1 = 0
interruptCounter2 = 0
 
timer1 = machine.Timer(0)  
timer2 = machine.Timer(1)  
 
def handleInterrupt1(timer1): #꼭 timer1을 써야함
  global interruptCounter1
  interruptCounter1 = interruptCounter1+1
  led1.value(not led1.value())
  #print("Interrupt has occurred1: " + str(interruptCounter1))
 
timer1.init(period=500, mode=machine.Timer.PERIODIC, callback=handleInterrupt1)

def handleInterrupt2(timer2): #꼭 timer2를 써야함
  global interruptCounter2
  interruptCounter2 = interruptCounter2+1
  led2.value(not led2.value())
  #print("Interrupt has occurred2: " + str(interruptCounter2))
 
timer2.init(period=250, mode=machine.Timer.PERIODIC, callback=handleInterrupt2)

# UART(0) is disabled (dedicated to REPL)
# UART(1) is null
# UART(2) is AUX port
uart = UART(2, 115200) # 1st argument: UART number: Hardware UART #1
# Write
#uart.write("esp32\n")
# Read
#print(uart.read()) # Read as much as possible using


while True:
    #pass
    uart.write("esp32esp32esp32esp32esp32\r\n")
    sleep(0.5)

'''
#https://randomnerdtutorials.com/micropython-esp32-deep-sleep-wake-up-sources/

# connecting... 하고 통신안될 때 esp32 보드에 EN tact 스위치를 눌렀다 놓는다.
MicroPython v1.17 on 2021-09-02; ESP32 module with ESP32
Type "help()" for more information.
>>> Connecting to /dev/ttyUSB1...
# 그럼 터미널에  표시가 뜬다.

터미널에 reboot라고 뜨면 EN 버튼 스위치를 누른다.
'''
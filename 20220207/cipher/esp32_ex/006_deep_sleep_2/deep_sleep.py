
from machine import Pin, SoftI2C, Timer, deepsleep
from time import sleep
# Importing the Timer subclass from the threading Class
from ssd1306 import SSD1306_I2C

# ------------------------------------------------------------------------------
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 32
oled = SSD1306_I2C(oled_width, oled_height, i2c)

# ------------------------------------------------------------------------------
led = Pin (2, Pin.OUT)
led1 = Pin (19, Pin.OUT)
led2 = Pin (23, Pin.OUT)

#blink LED
led.value(1)
sleep(0.5)
led.value(0)
sleep(0.5)

# ------------------------------------------------------------------------------
# period=1000 == 1000ms.
#timer = Timer(period=1000, mode=Timer.PERIODIC, callback=lambda t:print("Welcome to Microcontrollerslab"))
timer1=Timer(-1)
timer2=Timer(-2)
timer1.init(period=500, mode=Timer.PERIODIC, callback=lambda t:led1.value(not led1.value()))
timer2.init(period=250, mode=Timer.PERIODIC, callback=lambda t:led2.value(not led2.value()))
# ------------------------------------------------------------------------------
# wait 5 seconds so that you can catch the ESP awake to establish a serial communication later
# you should remove this sleep line in your final script
sleep(5)

oled.text("Im awake, but Im going to sleep", 0, 0)

oled.show()
print('Im awake, but Im going to sleep')

#sleep for 10 seconds (10000 milliseconds)
# deepsleep를 만나면 지정된 시간 10초(10000ms) 후에 모든 처리가 완전히 정지된다.
deepsleep(10000)

# led - d23, d19

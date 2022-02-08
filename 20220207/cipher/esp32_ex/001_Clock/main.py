from time import sleep
import ds1307
from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
ds = ds1307.DS1307(i2c)

# enable oscillator
ds.halt(False)
# set the datetime 12th Jan 2022 at 6:28:10 PM
now = (2022, 3, 12, 1, 18, 28, 10, 0)
ds.datetime(now)
# square wave output on pin SQ - 1Hz
ds.square_wave(1, 0)

ds.datetime()
print("I2C : " + str(ds.datetime()))

oled_width = 128
oled_height = 32
oled = SSD1306_I2C(oled_width, oled_height, i2c)

#oled.text("Hello, World!", 0, 0)
#oled.text("0123456789012345", 0, 8)
#oled.text("DAEONI-KANGUP 01", 0, 16)
#oled.text("keukmo.kang@gmai", 0, 24)
#oled.show()

led = Pin(2, Pin.OUT)

while True:
  d = str(ds.get_date())
  t = str(ds.get_time())

  Gdate = d[1]+d[2]+d[3]+d[4]+"-"+d[13]+d[14]+"-"+d[10]+d[11]
  Gtime = t[1]+t[2]+":"+t[5]+t[6]+":"+t[9]+t[10]

  led.value(not led.value())
  sleep(0.1)
  #print("I2C : " + str(ds.datetime()))
  oled.clear()
  oled.text(Gdate , 0, 0)
  oled.text(Gtime , 0, 24)
  oled.show()
  print(ds.get_date())
  print(ds.get_time())
# Download -> 파일 저장
# https://randomnerdtutorials.com/micropython-esp32-esp8266-vs-code-pymakr/


#This example uses https://github.com/adafruit/Adafruit_CircuitPython_AHTx0.git
# and initially was tested using a Sparkfun SparkX AHT20 Humidity + Temperature board	
# and Treedix JST/QWIIC breakout (https://www.amazon.com/dp/B09BF7YYBK)
#Brygg Ullmer, Clemson University
#Begun 2026-06-14

import time
import board
import busio
import adafruit_ahtx0

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_ahtx0.AHTx0(i2c)

sleepS = 10

updatePat = "- {temp: %.2f, relHumid: %.2f}"

while True:
  t, rh = sensor.temperature, sensor.relative_humidity
  updateStr = updatePat % (t, rh)
  print(updateStr)
  time.sleep(sleepS)

### end ###


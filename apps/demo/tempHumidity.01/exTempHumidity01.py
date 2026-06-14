#This example uses https://github.com/adafruit/Adafruit_CircuitPython_AHTx0.git
#and initially was tested using a Sparkfun SparkX AHT20 Humidity + Temperature board	

import board
import busio
import adafruit_ahtx0

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_ahtx0.AHTx0(i2c)

print(sensor.temperature, sensor.relative_humidity)

### end ###


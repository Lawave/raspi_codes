import time
import board
import busio
from adafruit_bme280 import basic as adafruit_bme280

i2c = busio.I2C(board.SCL, board.SDA)

bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

bme280.sea_level_pressure= 1013.25

while True:
    temp = bme280.temperature
    pres = bme280.pressure / 760
    print(temp)
    print(pres)
    time.sleep(1)
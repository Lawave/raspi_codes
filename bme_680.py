import time
import board
import busio
import adafruit_bme680

i2c = busio.I2C(board.SCL, board.SDA)

bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

while True:
    temp = bme680.temperature
    print(temp)
    time.sleep(1)
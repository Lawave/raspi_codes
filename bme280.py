import time
import board
import busio
from adafruit_bme280 import basic as adafruit_bme280

def get_bme280_data(bme280):
    temp = bme280.temperature
    pres = bme280.pressure
    payload_pres_altitude = 44330 * (1.0 - (pres/bme280.sea_level_pressure) ** (1/5.255))
    
    return temp,pres * 100, payload_pres_altitude

i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
bme280.sea_level_pressure= 1013.25
a, b, c = get_bme280_data(bme280)
while True:
    print(a)
    print("\n")
    print(b)
    print("\n")
    print(c)
    print("\n")
import time
import board
import busio
from adafruit_bme280 import basic as adafruit_bme280

def get_bme280_data(bme280):
    temp = bme280.temperature
    pres = bme280.pressure / 760
    return temp,pres
import time
import board
import busio
from adafruit_bme280 import basic as adafruit_bme280

def get_bme280_data(bme280):
    temp = bme280.temperature
    pres = bme280.pressure
    payload_pres_altitude = 44330 * (1.0 - (pres/bme280.sea_level_pressure) ** (1/5.255))
    
    return temp,pres * 100, payload_pres_altitude
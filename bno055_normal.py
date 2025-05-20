import time
import board
import busio
import adafruit_bno055

def get_bno055_data(bno055):
    euler = bno055.euler

    return euler[0], euler[1], euler[2]


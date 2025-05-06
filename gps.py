import time
import board
import busio
import adafruit_gps
import serial
import datetime
import socket
import struct
import math
import RPi.GPIO as GPIO
def gps_data():
    now = datetime.datetime.now()
    now_ = now.replace(microsecond=0) 
    gps.update()
    if gps.speed_knots is not None:
        gps_speed_knots = float(gps.speed_knots)
    else:
        gps_speed_knots = 0.0
    if gps.altitude_m is not None:
        gps_altitude_m = float(gps.altitude_m)
    else:
        gps_altitude_m = 0.0
    return gps_speed_knots, gps_altitude_m, gps.longitude, gps.latitude, gps.has_fix, now_



uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=10)
gps = adafruit_gps.GPS(uart, debug=False)  
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
gps.send_command(b"PMTK220,1000")

try:
    while True:
        gps_knots, gps_altitude_m, gps_longitude, gps_latitude, gps_has_fix, now_ = gps_data()
        print(f"{now_},{gps_knots},{gps_longitude},{gps_latitude},{gps_altitude_m}")

        time.sleep(2)
        
except KeyboardInterrupt:
    GPIO.cleanup()

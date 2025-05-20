import time
import adafruit_gps
import serial
import datetime
import RPi.GPIO as GPIO


def get_gps_data(gps):
    now = datetime.datetime.now()
    now_ = now.replace(microsecond=0) 
    gps.update()
    gps_has_fix = gps.has_fix
    
    if gps_has_fix == False:
        gps_altitude  = 0.0
        gps_longitude   = 0.0
        gps_latitude    = 0.0
    
    else:
        gps_longitude = float(gps.longitude)
        gps_latitude = float(gps.latitude)
        gps_altitude = float(gps.altitude_m)

    return gps_longitude, gps_latitude, gps_altitude, now_
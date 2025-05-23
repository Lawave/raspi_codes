import time
import adafruit_gps
import serial
import datetime
import RPi.GPIO as GPIO


def get_gps_data(gps):
    now = datetime.datetime.now()
    now_ = now.replace(microsecond=0)
    gps_time_send = now_.timestamp()
    gps.update()
    gps_has_fix = gps.has_fix
    
    if gps_has_fix == False:
        gps_altitude  = -1.0
        gps_longitude   = -1.0
        gps_latitude    = -1.0
    
    else:
        gps_longitude = float(gps.longitude)
        gps_latitude = float(gps.latitude)
        gps_altitude = float(gps.altitude_m)

    return gps_longitude, gps_latitude, gps_altitude, gps_time_send
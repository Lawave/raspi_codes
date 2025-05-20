import time
import board
import busio
import adafruit_bno055
from adafruit_bme280 import basic as adafruit_bme280
import adafruit_gps
import serial
import datetime
import socket
import struct
import math
import RPi.GPIO as GPIO
from bme_680 import get_bme280_data
from bno055_normal import get_bno055_data
from gps import get_gps_data
from picamera2 import Picamera2
from PIL import Image
import io
from flask import Flask, Response
import threading
from kamera import start_video_server
import pigpio
from b_servo import turn_servo
from buzzer import buzzer
from multiprocessing import Process

#GPS Setup
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=10)
gps = adafruit_gps.GPS(uart, debug=False)  
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
gps.send_command(b"PMTK220,1000")

#BNO055 Setup
i2c = busio.I2C(board.SCL, board.SDA)
bno055 = adafruit_bno055.BNO055_I2C(i2c)

#BME280 Setup
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
bme280.sea_level_pressure= 1013.25

#Servo Setup and Calculated Degrees
servo = pigpio.pi()
servo_pin = 13
deg_1 = 0.2755
deg_2 = 0.55
deg_3 = 0.802

#Buzzer Setup
buzzer_pin = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)

'''
Starting camera with process
It uses different core for camera
It prevents camera to block other codes
'''
host = "0.0.0.0"
port = 5005
video_process = Process(target=start_video_server, args=(host,port))
video_process.start()

count = 0
check = 1
while True:
    #Getting sensor datas
    temp,pres = get_bme280_data(bme280)
    yaw, roll, pitch = get_bno055_data(bno055)
    gps_longitude, gps_latitude, gps_altitude, now = get_gps_data(gps)
    
    print(f"Temp: {temp}, Pressure = {pres}\n")
    print(f"Yaw: {yaw}, Roll: {roll}, Pitch: {pitch}\n")
    print(f"Longitude: {gps_longitude}, Latitude: {gps_latitude}, Altitude: {gps_altitude}, Time {now}\n\n")
    
    if ((count > 10) and (check)):
        turn_servo(deg_1,servo,servo_pin)
        buzzer(buzzer_pin)
        check = 0
    time.sleep(2)
    count += 1

 
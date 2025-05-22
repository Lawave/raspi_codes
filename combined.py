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
from bme280 import get_bme280_data
from bno055_normal import get_bno055_data
from gps import get_gps_data
from picamera2 import Picamera2
from PIL import Image
import io
from flask import Flask, Response
import threading
from kamera import start_video_server
import pigpio
from servo_1 import turn_servo
from buzzer import buzzer
from multiprocessing import Process
import csv
import os
from save_sd_telemetry import csv_file_reset,csv_file_write

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
deg_90 = 0.2755
deg_180 = 0.55
deg_270 = 0.802

#Buzzer Setup
buzzer_pin = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)

'''
Starting camera with process
It uses different core for camera
It prevents camera to block other codes
'''
host = "172.20.10.3"
port = 5005
video_process = Process(target=start_video_server, args=(host,port))
video_process.start()

#UDP Setup
udp_ip = "172.20.10.2"
udp_port = 5000
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



packet_number = 0
check = 1

team_no = 3202951

csv_file_reset()

while True:
    #Getting sensor datas
    payload_temp,payload_pres, payload_pres_altitude = get_bme280_data(bme280)
    yaw, roll, pitch = get_bno055_data(bno055)
    gps_longitude, gps_latitude, gps_altitude, gps_time = get_gps_data(gps)
    packet_number += 1
    
    print(f"Temp: {payload_temp}, Pressure = {payload_pres} Pressure Altitude = {payload_pres_altitude} \n")
    print(f"Yaw: {yaw}, Roll: {roll}, Pitch: {pitch}\n")
    print(f"Longitude: {gps_longitude}, Latitude: {gps_latitude}, Altitude: {gps_altitude}, Time {gps_time}\n\n")
    
    telemetry_data = {
        packet_number,
        "NULL", #Satellite status it will add later
        "NULL", #Error Code it will add later
        gps_time,
        payload_pres,
        "NULL", #Carrier Pressure it will add later
        payload_pres_altitude, 
        "NULL", #Carrier altitude it will add later
        "NULL", #Altitude diff it will add later
        "NULL", #Descent Velocity it will add later
        payload_temp,
        "NULL", #Battery Voltage it will add later
        gps_latitude,
        gps_longitude,
        gps_altitude,
        pitch,
        roll,
        yaw,
        "NULL", #RHRH it will add later
        "NULL", #IoT temp 1 data it will add later
        "NULL", #IoT temp 2 data it will add later
        team_no
        }
    
    csv_file_write(telemetry_data)
    
    udp_data = struct.pack(
            '>Hdffffffff',
            packet_number,
            gps_time,
            payload_pres,
            payload_temp,
            gps_latitude,
            gps_longitude,
            gps_altitude,
            pitch,
            roll,
            yaw
        )
    udp_socket.sendto(udp_data, (udp_ip,udp_port))
    if ((packet_number > 10) and (check)):
        turn_servo(deg_90,servo,servo_pin)
        buzzer(buzzer_pin)
        check = 0
    
    time.sleep(1)


 
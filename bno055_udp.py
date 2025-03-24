import time
import board
import busio
import adafruit_bno055
import socket
import struct

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055_I2C(i2c)

UDP_IP = "192.168.183.74" 
UDP_PORT = 5005 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    try:
        gyro = sensor.euler

        if gyro is not None:
            data = struct.pack("fff", gyro[0], gyro[1], gyro[2])
            
            sock.sendto(data, (UDP_IP, UDP_PORT))

            print(f"gyro: {gyro}")
        
        else:
            print("gönderilemedi")
    finally:
      time.sleep(1)  # 100ms bekle (UDP trafiğini azaltmak için)

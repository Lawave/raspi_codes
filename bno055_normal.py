import time
import board
import busio
import adafruit_bno055

i2c = busio.I2C(board.SCL, board.SDA)

sensor = adafruit_bno055.BNO055_I2C(i2c)

while True:
    acceleration = sensor.acceleration  
    magnetic = sensor.magnetic  
    gyro = sensor.gyro  

    print(f"Accel: {acceleration[0], {acceleration[1]}, {acceleration[2]}}")
    print(f"Gyro: {gyro[0]},{gyro[1]},{gyro[2]}")
    time.sleep(1)

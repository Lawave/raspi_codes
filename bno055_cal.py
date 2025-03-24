import time
import board
import busio
import adafruit_bno055

i2c = busio.I2C(board.SCL, board.SDA)

sensor = adafruit_bno055.BNO055_I2C(i2c)

while True:
    sys, gyro, accel, mag = sensor.calibration_status
    #manyetik alan kalibrasyonu için 8 şeklinde gezdirmek gerekiyo
    #gyro kalibrasonu için belirli bir yerde sabit durması yetiyo
    #accel kalibrasyonu içinse x y ve z düzlemlereinin + ve - kısmına bakması ve o anlarda sabit olması gerekiyo
    #yani bi küpün yüzeylerine oturtmak gibi oluyo
    print(f"Gyro:{gyro}, Mag:{mag}, Accel:{accel}")
    
    if gyro == 3 and accel == 3 and mag == 3:
        print("Kalibrasyon tamamlandı")
        
    time.sleep(1)
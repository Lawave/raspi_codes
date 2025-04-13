import time
import board
import busio
import adafruit_bno055
import os

# I2C başlat
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055_I2C(i2c)

# Dosya yolu (SD kartın mount edildiği yere göre ayarla, örn: /media/pi/SDCARD/)
log_dir = "/home/javid/bno055_logs"
os.makedirs(log_dir, exist_ok=True)
filename = os.path.join(log_dir, "sensor_log.csv")

# Başlıkları yaz
with open(filename, "w") as f:
    f.write("Time(s),Accel_X,Accel_Y,Accel_Z,Gyro_X,Gyro_Y,Gyro_Z\n")

print("Veri kaydı başladı... Dosya:", filename)

start_time = time.time()

try:
    while True:
        now = time.time() - start_time
        accel = sensor.acceleration  # (x, y, z)
        gyro = sensor.gyro  # (x, y, z)

        if accel and gyro:
            line = f"{now:.2f},{accel[0]},{accel[1]},{accel[2]},{gyro[0]},{gyro[1]},{gyro[2]}\n"
            with open(filename, "a") as f:
                f.write(line)
            print(line.strip())

        time.sleep(1)  # 10 Hz örnekleme

except KeyboardInterrupt:
    print("Kayıt durduruldu.")


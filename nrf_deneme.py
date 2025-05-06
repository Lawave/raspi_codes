import socket
import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import spidev
import time

# GPIO ayarı
GPIO.setmode(GPIO.BCM)

# NRF Ayarları
pipes = [[0xE7, 0xE7, 0xE7, 0xE7, 0xE7]]  # Alıcıda da aynı olmalı

radio = NRF24(GPIO, spidev.SpiDev())
radio.begin(0, 17)  # CSN = CE0(GPIO8), CE = GPIO17
radio.setRetries(15,15)
radio.setPayloadSize(32)
radio.setChannel(0x76)
radio.setDataRate(NRF24.BR_1MBPS)
radio.setPALevel(NRF24.PA_MIN)
radio.openWritingPipe(pipes[0])
radio.stopListening()

# UDP dinleyici ayarı
UDP_IP = "0.0.0.0"     # Tüm IP’lerden veri al
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"UDP port {UDP_PORT} üzerinden veri dinleniyor...")

try:
    while True:
        data, addr = sock.recvfrom(1024)
        received = data.decode().strip()
        print(f"Gelen UDP verisi: {received}")
        message = list("1")
        while len(message) < 32:
            message.append(0)  # 32 bayta tamamla

        result = radio.write(message)
        if result:
            print("NRF ile '1' gönderildi.")
        else:
            print("NRF gönderim başarısız.")
            
        time.sleep(1)

except KeyboardInterrupt:
    print("Program sonlandırılıyor...")
finally:
    GPIO.cleanup()
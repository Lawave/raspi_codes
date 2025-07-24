import spidev
import time

spi = spidev.SpiDev()
spi.open(0, 0) # /dev/spidev0.0 için (bus 0, device 0)

# SPI ayarlarını yapılandırın (WM1302 için geçerli olabilir)
spi.max_speed_hz = 1000000  # 1 MHz (cihazınızın desteklediği hıza göre ayarlayın)
spi.mode = 0b00             # SPI Modu 0 (WM1302 için kontrol edin)

try:
    # Test için bir byte gönderip almayı deneyin
    # Bu, bağlı bir cihaz olmadan başarılı olmayabilir, ancak
    # temel iletişimin başlatılıp başlatılamadığını gösterir.
    
    # Örneğin, bir okuma komutu göndermeyi deneyelim (genellikle ilk byte komut olur)
    # Bu sadece bir deneme amaçlıdır, gerçek bir LoRaWAN komutu değildir.
    data_to_send = [0x01, 0x00, 0x00, 0x00] # Rastgele bir veri
    print(f"Gönderilen veri: {[hex(b) for b in data_to_send]}")
    
    resp = spi.xfer2(data_to_send)
    print(f"Alınan veri: {[hex(b) for b in resp]}")

except Exception as e:
    print(f"SPI iletişiminde hata: {e}")
finally:
    spi.close()
    print("SPI portu kapatıldı.")
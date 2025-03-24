import smbus2
import time

# INA219 I2C adresi (genellikle 0x40)
INA219_I2C_ADDR = 0x40

# Register adresleri
SHUNT_VOLTAGE_REGISTER = 0x01  # Shunt voltage register (16-bit)

# I2C arayüzünü başlat (Raspberry Pi için I2C-1)
bus = smbus2.SMBus(1)

def read_shunt_voltage():
    """INA219'dan shunt voltajını (mV) okur"""
    raw_data = bus.read_word_data(INA219_I2C_ADDR, SHUNT_VOLTAGE_REGISTER)

    # Byte sıralamasını düzelt (Little Endian formatta olduğu için)
    raw_data = ((raw_data & 0xFF) << 8) | (raw_data >> 8)

    # Negatif değerleri düzelt (2'nin komplemanı kullanıyor)
    if raw_data > 32767:
        raw_data -= 65536

    # Shunt voltajı (10µV per bit, yani 0.00001V = 10µV)
    shunt_voltage_mV = raw_data * 0.01

    return shunt_voltage_mV

# Sonsuz döngüde okuma yap
while True:
    try:
        vshunt = read_shunt_voltage()
        print(f"Shunt Voltajı: {vshunt:.3f} mV")
    except Exception as e:
        print(f"Hata: {e}")
    
    time.sleep(1)  # 1 saniye bekle
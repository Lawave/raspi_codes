import serial
import pynmea2

# GPS modülünün bağlı olduğu seri portu belirt (örnek: /dev/ttyS0 ya da /dev/serial0)
port = "/dev/serial0"
baudrate = 9600  # SAM-M8Q için varsayılan baudrate

try:
    # Seri bağlantıyı başlat
    ser = serial.Serial(port, baudrate, timeout=1)
    print(f"GPS portu {port} üzerinden dinleniyor...")

    while True:
        line = ser.readline().decode('ascii', errors='replace').strip()

        if line.startswith('$'):
            try:
                msg = pynmea2.parse(line)
                
                # Sadece GGA veya RMC cümlelerini işliyoruz
                if isinstance(msg, pynmea2.GGA) or isinstance(msg, pynmea2.RMC):
                    print(f"Zaman: {msg.timestamp}, Enlem: {msg.latitude} {msg.lat_dir}, Boylam: {msg.longitude} {msg.lon_dir}")
            except pynmea2.ParseError:
                continue

except serial.SerialException as e:
    print(f"Seri bağlantı hatası: {e}")

except KeyboardInterrupt:
    print("\nGPS verisi alımı durduruldu.")

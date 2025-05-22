import csv
import os

def csv_file_reset():
    csv_file_road = "/home/mete/raspi_codes/sensor_data.csv"
    with open(csv_file_road, mode='w', newline='') as file:
        file_writer = csv.writer(file)
        
        file_writer.writerow([
            "Paket Numarası",
            "Uydu Statüsü",
            "Hata Kodu",
            "Gönderme Saati",
            "Basınç1",
            "Basınç2",
            "Yükseklik1",
            "Yükseklik2",
            "İrtifa Farkı",
            "İniş Hızı",
            "Sıcaklık",
            "Pil Gerilimi",
            "GPS1 Latitude",
            "GPS1 Longitude",
            "GPS1 Altitude",
            "Pitch",
            "Roll",
            "Yaw",
            "RHRH",
            "IoT S1 Data",
            "IoT S2 Data",
            "Takım NO"
            ])
    
        
    
def csv_file_write(telemetry_data):
    csv_file_road = "/home/mete/raspi_codes/sensor_data.csv"
    with open(csv_file_road, mode='a', newline='') as file:
        file_writer = csv.writer(file)
        
        file_writer.writerow(telemetry_data)
    
import socket
import struct



def send_telemetry_udp(udp_ip, udp_port, udp_socket, telemetry_data):
    udp_data = struct.pack(
            '>HdfffffffffI',
            telemetry_data[0],  #Packet number
            #telemetry_data[1],  #Satellite status 
            #telemetry_data[2],  #Error Code
            telemetry_data[3],  #GPS Timestamp
            telemetry_data[4],  #Payload Pressure
            #telemetry_data[5],  #Carrier Pressure
            telemetry_data[6],  #Payload Altitude 
            #telemetry_data[7],  #Carrier Altitude
            #telemetry_data[8],  #Altitude Difference
            #telemetry_data[9],  #Descent Velocity
            telemetry_data[10], #Payload Temperature
            #telemetry_data[11], #Payload Voltage
            telemetry_data[12], #Latitude
            telemetry_data[13], #Longitude
            telemetry_data[14], #GPS Altitude
            telemetry_data[15], #Pitch
            telemetry_data[16], #Roll  
            telemetry_data[17], #Yaw
            #telemetry_data[18], #RHRH 
            #telemetry_data[19], #IoT S1 Data 
            #telemetry_data[20], #IoT S2 Data
            telemetry_data[21]  #Team NO
        )
    udp_socket.sendto(udp_data, (udp_ip,udp_port))

    
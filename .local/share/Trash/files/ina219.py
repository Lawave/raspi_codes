import time
from ina219 import INA219, DeviceRangeError

# Define the INA219 sensor with a shunt resistor value (default is 0.1 ohm)
SHUNT_OHMS = 0.1
ina = INA219(SHUNT_OHMS)
ina.configure()

while True:
    try:
        bus_voltage = ina.voltage()  # Voltage on V+ pin
        current = ina.current()  # Current in mA
        power = ina.power()  # Power in mW

        print(f"Bus Voltage: {bus_voltage:.2f} V")
        print(f"Current: {current:.2f} mA")
        print(f"Power: {power:.2f} mW")
        print("-" * 30)

    except DeviceRangeError as e:
        print("Current out of range:", e)

    time.sleep(1)  # Wait before the next reading

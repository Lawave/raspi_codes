

import RPi.GPIO as GPIO
import time

BUTTON_PIN = 17  # GPIO17 (pin 11)
BUZZER_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUZZER_PIN,GPIO.OUT)
GPIO.output(BUZZER_PIN, GPIO.LOW)
print("Butona basılmasını bekliyorum...")
try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            print("Butona basıldı!")
            
        else:
            pass
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()


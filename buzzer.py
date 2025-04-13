import RPi.GPIO as GPIO
import time

BUZZER_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.output(BUZZER_PIN, GPIO.LOW)
time.sleep(0.5)
print("high")
GPIO.output(BUZZER_PIN, GPIO.HIGH)
time.sleep(5)
print("finish")

GPIO.cleanup()



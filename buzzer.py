import RPi.GPIO as GPIO
import time
buzzer_pin = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)
def buzzer(buzzer_pin):
    GPIO.output(buzzer_pin, GPIO.LOW)
    time.sleep(1)
    GPIO.output(buzzer_pin, GPIO.HIGH)
    GPIO.cleanup()


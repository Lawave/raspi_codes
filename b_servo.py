import time
import pigpio

pi = pigpio.pi()
servo_pin = 18

def turn_servo(duration):
    pi.set_servo_pulsewidth(servo_pin, 1200)
    time.sleep(duration)
    pi.set_servo_pulsewidth(servo_pin, 1500)
turn_servo(0.2755)
pi.set_servo_pulsewidth(servo_pin, 0)
pi.stop()
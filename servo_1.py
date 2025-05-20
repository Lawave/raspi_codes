import time
import pigpio

def turn_servo(duration,servo,servo_pin):
    servo.set_servo_pulsewidth(servo_pin, 1200)
    time.sleep(duration)
    servo.set_servo_pulsewidth(servo_pin, 1500)
    servo.set_servo_pulsewidth(servo_pin, 0)
    servo.stop()
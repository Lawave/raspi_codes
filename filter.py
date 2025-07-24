import time
import pigpio
from servo_1 import turn_servo
import threading
def mechanic_filter(SERVO_GPIO_1,SERVO_GPIO_2,rhrh_code):
    def run_parallel(duration_1,SERVO_GPIO_1,duration_2,SERVO_GPIO_2):
        t1 = threading.Thread(target = turn_servo, args=(duration_1,pi,SERVO_GPIO_1))
        t2 = threading.Thread(target = turn_servo, args=(duration_2,pi,SERVO_GPIO_2))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    pi = pigpio.pi()
    combinations = {    
    "M": (90,90),
    "F": (180,180),   
    "N": (270,270),
    "R": (90,0),
    "G": (180,0),
    "B": (270,0),
    "P": (90,270),
    "Y": (90,180),
    "C": (180,270)
    }

    servo_angles_1 = {
        0: 0,
        90: 0.25,
        180: 0.53,
        270: 0.85,
        360: 1.1
    }
    servo_angles_2 = {
        0: 0,
        90: 0.25,
        180: 0.51,
        270: 0.72,
        360: 1
    }
    timer_start = time.time()

    color_1 = rhrh_code[1]
    print("1")
    run_parallel(
        servo_angles_1[combinations[color_1][0]], SERVO_GPIO_1,
        servo_angles_2[combinations[color_1][1]], SERVO_GPIO_2
    )

    elapsed = time.time() - timer_start
    time.sleep(int(rhrh_code[0]) - elapsed)

    color_2 = rhrh_code[3]
    print("2")
    std_servo_1 = 360 - combinations[color_1][0]
    std_servo_2 = 360 - combinations[color_1][1]

    run_parallel(
        servo_angles_1[std_servo_1], SERVO_GPIO_1,
        servo_angles_2[std_servo_2], SERVO_GPIO_2
    )
    time.sleep(5)

    timer_start = time.time()
    print("3")
    run_parallel(
        servo_angles_1[combinations[color_2][0]], SERVO_GPIO_1,
        servo_angles_2[combinations[color_2][1]], SERVO_GPIO_2
    )
    
    elapsed = time.time() - timer_start
    time.sleep(int(rhrh_code[2]) - elapsed)

    std_servo_1 = 360 - combinations[color_2][0]
    std_servo_2 = 360 - combinations[color_2][1]
    print("4")
    run_parallel(
        servo_angles_1[std_servo_1], SERVO_GPIO_1,
        servo_angles_2[std_servo_2], SERVO_GPIO_2
    )
    pi.stop()


mechanic_filter(18,19,"7R8Y")
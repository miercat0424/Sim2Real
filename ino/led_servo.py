import pyfirmata
import os 
import cv2
import numpy as np
import time

from multiprocessing import Process
from color_check import color_check
from threading_method import ths

os.chdir('/home/minwoo')
board = pyfirmata.Arduino('/dev/ttyACM0')
it = pyfirmata.util.Iterator(board)
it.start()

# global
arr = np.vstack([np.zeros(3),np.zeros(3)])
swi = True

G_inp = board.get_pin('d:8:i')
Y_inp = board.get_pin('d:9:i')

G_led = board.get_pin('d:13:o')
Y_led = board.get_pin('d:12:o')
servo = board.get_pin("d:3:s")

class Servo_Control :  
    def __init__(self, DELAY):
        self.DELAY= DELAY

    def move_servo(self,Position):
        if Position == 180 :
            servo.write(Position)
            board.pass_time(self.DELAY)
        elif Position == 0 : 
            servo.write(Position)
            board.pass_time(self.DELAY)
        else :
            servo.write(Position)
            board.pass_time(self.DELAY)


def color_check(*args):

    global arr, swi
    count = 0
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,480)

    while True:
        count += 1
        _, frame = cap.read()
        height, width, _ = frame.shape

        cx = int(width/2)
        cy = int(height/2)

        pixel_center = frame[cy,cx]
        arr = np.vstack([arr,pixel_center])

        cv2.circle(frame, (cx,cy), 5, (255,0,0,),3)

        cv2.imshow("Frame",frame)
        key = cv2.waitKey(1)
        if count % 10 == 0 :
            arr = np.vstack([np.zeros(3),np.zeros(3)])

        if key == 27 :
            swi = False
            break

    cap.release()
    cv2.destroyAllWindows()

    return

def see(*args):
    global arr
    while True :
        obj = arr[-1]
        if  0 < obj[0] < 20 and 0 < obj[1] < 20 and 0 < obj[2] < 20 :
            print()
        elif obj[0] == 0 and obj[1] == 0 and obj[2] == 0 :
            pass
        else : 
            r=1
        
        if swi == False :
            break

def led_control(*args):
    while True : 
        value = G_inp.read()
        G_led.write(value)
    

DELAY   = 1
MIN     = 0
MAX     = 180
MID     = 90

# th1 = ths(1, "Th-1", color_check, (0))
# th2 = ths(2, "Th-2", see, (0))
# th3 = ths(3, 'Th-3', led_control, (0))

# th1.start()
# th2.start()
# th3.start()

# th1.join()
# th2.join()

# Servo_Control(DELAY).move_servo(180)


while True:
    Servo_Control(DELAY).move_servo(MIN)
    Servo_Control(DELAY).move_servo(MAX)
    Servo_Control(DELAY).move_servo(MID)
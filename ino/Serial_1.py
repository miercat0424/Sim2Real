from cmath import nan
import serial
import os 
import re
import numpy as np

os.chdir('/home/minwoo')
ser = serial.Serial('/dev/ttyACM0')
arr = np.array([])
i = 0

for _ in range(1000) :
    i+=1
    try :
        aurduinoData = ser.readline().decode('ascii')
        Ax = np.array(aurduinoData.split())[3]
        Ay = np.array(aurduinoData.split())[7]
        if Ax or Ay == nan :
            os.chdir('/home/minwoo/code_examples/ino')
            os.system("python Serial_1.py")
            print("Restarting ...")
        print(Ax, Ay)
    except UnicodeDecodeError :
        pass
    except IndexError :
        pass
    except ValueError :
        pass








    
import matplotlib.pyplot as plt
import serial
import time
import os 
os.chdir('/home/minwoo')
arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=.1)
# def write_read(x):
#     arduino.write(bytes(x, 'utf-8'))
#     time.sleep(.05)
#     data = arduino.readline()
#     return data

data = []
for i in range(50):
    line=arduino.readline()
    if line :
        string = line.decode()
        num = int(string)
        print(num)
        data.append(num)
arduino.close()        

plt.plot(data)
plt.xlabel("Time")
plt.ylabel("Potentiometer Reading")
plt.title('Potentiometer Reading vs. Time')
plt.show()

# while True:
#     num = input("Enter a number : ")
#     value = write_read(num)
#     print(value)
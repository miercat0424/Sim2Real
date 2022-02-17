import pyfirmata
import os 

os.chdir('/home/minwoo')
board = pyfirmata.Arduino('/dev/ttyACM0')
it = pyfirmata.util.Iterator(board)
it.start()

four_inp = board.get_pin('a:4:i')
five_inp = board.get_pin('a:5:i')
dtwo_inp = board.get_pin('d:2:i')

while True:
    print(four_inp.read())
    print(five_inp.read())
    print(dtwo_inp.read())

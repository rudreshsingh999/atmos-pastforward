from Arduino import Arduino
import time

board = Arduino('9600',port="/dev/ttyACM0") #plugged in via USB, serial com at rate 9600
board.pinMode(9, "OUTPUT")
board.pinMode(3, "INPUT")
file = open("output1.txt", 'w+')
f=0
while True:
    r=board.digitalRead(3)
    while (r==1):
    	if(f==0):
    		file.write("Switch is ON\n")
    		f=1
        r=board.digitalRead(3)
        board.digitalWrite(9,"HIGH")
        print(board.analogRead(3))
        #file.write("this is line" + str(r))
    board.digitalWrite(9,"LOW")
    if(f==1):
    	file.write("Switch is OFF\n")
    	f=0
file.close()
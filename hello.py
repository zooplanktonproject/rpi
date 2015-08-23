from time import sleep
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

FRAME_DELAY = 0.0030
START_CHAR = "@"
END_CHAR = "#"

def setColor(r, g, b):
  str = START_CHAR

  for x in range(1, 91):
    str += "{0:0>3}{1:0>3}{2:0>3}{3:0>3}".format(x, r, g, b)

  str += END_CHAR

  print str
  #ser.write(str);
  sleep(FRAME_DELAY)

setColor(255, 0, 0);

from time import sleep
import serial
import numpy as np

ser = serial.Serial('/dev/ttyACM0', 9600)

NODE_COUNT = 98
FRAME_DELAY = 0.0030
START_CHAR = "@"
END_CHAR = "#"

def sendFrame(values):
  str = START_CHAR

  for x, colors in enumerate(values):
    str += "{0:0>3}{1:0>3}{2:0>3}{3:0>3}".format(x + 1, colors[0], colors[1], colors[2])

  str += END_CHAR
  print str
  ser.write(str)
  sleep(FRAME_DELAY)

for y in range(2):

  for x in range(NODE_COUNT):

    values = np.zeros(shape=(NODE_COUNT, 3), dtype=np.uint8)

    values[x] = [255, 0, 0]

    sendFrame(values)
    sleep(1)

    values[x] = [0, 255, 0]
    sendFrame(values)
    sleep(1)

    values[x] = [0, 0, 255]
    sendFrame(values)
    sleep(1)


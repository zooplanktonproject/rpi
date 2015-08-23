#!/usr/bin/python
from zoo import Zoo
from time import sleep

z = Zoo()

def setColor(r, g, b):

  for x in range(1, 89):
    z.update_node(x, [r, g, b])

  z.send_frame()


setColor(0, 0, 0)
sleep(1)

while True:
  setColor(255, 0, 0)
  sleep(1)
  setColor(0, 255, 0)
  sleep(1)
  setColor(0, 0, 255)
  sleep(1)

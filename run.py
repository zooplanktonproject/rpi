#!/usr/bin/python
from zoo import Zoo
from time import sleep

z = Zoo()

def set_color(r, g, b):

  for x in range(1, 89):
    z.set_node(x, [r, g, b])

  z.send_frame()


set_color(0, 0, 0)
sleep(1)

while True:
  set_color(255, 0, 0)
  sleep(1)
  set_color(0, 255, 0)
  sleep(1)
  set_color(0, 0, 255)
  sleep(1)

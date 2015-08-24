#!/usr/bin/python
from zoo import Zoo
from time import sleep
from random import randint

z = Zoo()

def set_color(color):

  for x in range(z.NODE_COUNT):
    z.set_node(x, [color[0], color[1], color[2]])

  z.send_frame()


set_color([0, 0, 0])
sleep(1)

while True:
  color = [randint(0, 255), randint(0, 255), randint(0, 255)]
  set_color(color)
  sleep(1)
  #set_color([255, 0, 0])
  #sleep(1)
  #set_color([0, 255, 0])
  #sleep(1)
  #set_color([0,0,255])
  #sleep(1)

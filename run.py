#!/usr/bin/python
from zoo import Zoo
from time import sleep
import json

z = Zoo()


with open('./data/frames/mKI9lgC8ALsGs.json') as data_file:
  data = json.load(data_file)


while True:
  for frame in data['data']:
    z.set_frame(frame)
    z.send_frame()

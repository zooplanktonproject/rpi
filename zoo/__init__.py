import numpy as np
import output
import time
import json


class Zoo:
  # spire is considered a node at position zero
  NODE_COUNT = 45
  START_CHAR = "@"
  END_CHAR = "#"
  FRAME_DELAY = 0.0030
  NODE_BRIGHTNESS = 100
  # ndarray data type, max int is 255 * 100 (uint8 * max brightness)
  NDTYPE=np.int16

  def __init__(self):
    self.reset_frame()
    self.frame_data = []

  def init_frame(self):
    return np.zeros(shape=(self.NODE_COUNT, 3), dtype=self.NDTYPE)

  def reset_frame(self):
    self.frame = self.init_frame()

  def send_frame(self):
    serial_array = []

    serial_array.append(self.START_CHAR)

    frame = self.limit_brightness()

    for x, colors in enumerate(frame):
      serial_array.append("{0:0>3}{1:0>3}{2:0>3}{3:0>3}".format(x, colors[0], colors[1], colors[2]))

    serial_array.append(self.END_CHAR)

    output.write("".join(serial_array))

    self.frame_delay()

  def set_node(self, pos, color=[0, 0, 0]):
    self.frame[pos] = color

  def set_frame(self, frame_array):
    # warning: can fuck shit up right here
    self.frame = np.asarray(frame_array, dtype=self.NDTYPE)

  def limit_brightness(self):
    return np.copy(self.frame).__mul__(self.NODE_BRIGHTNESS).__div__(100)

  def frame_delay(self):
    time.sleep(self.FRAME_DELAY)

  # gget some sleep asshole
  def fade_out(self):
    iterations = 100
    for x in iterations:
      self.frame -= x

  def load_frames(self, filename):
    with open('./data/frames/' + filename + '.json') as data_file:
     self.frame_data = json.load(data_file)

  def animate(self, filename, play_iterations):

    self.play_number = 0
    self.frame_number = 0
    self.spire_last_message_at_frame = 0
    self.reset_frame()
    self.load_frames(filename)

    for i in range(play_iterations):
      for frame in self.frame_data['data']:
        self.set_frame(frame)
        self.send_frame()
        self.frame_number += 1

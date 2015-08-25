import numpy as np
import output
from time

class Zoo:
  # spire is considered a node at position zero
  NODE_COUNT = 90
  START_CHAR = "@"
  END_CHAR = "#"
  FRAME_DELAY = 0.0030
  NODE_BRIGHTNESS = 0.8
  # .7 prevents white flicker, perhaps implement that elsewhere though as a limit?
  SPIRE_BRIGHTNESS = 0.7

  def __init__(self):
    self.reset_frame()

  def init_frame(self):
    return np.zeros(shape=(self.NODE_COUNT, 3), dtype=np.uint8)

  def reset_frame(self):
    self.frame = self.init_frame()

  def send_frame(self):
    serial_array = []

    serial_array.append(self.START_CHAR)

    for x, colors in enumerate(self.frame):

      if x == 0:
        r = self.limit_spire_bright(colors[0])
        g = self.limit_spire_bright(colors[1])
        b = self.limit_spire_bright(colors[2])

        output.write("${0:0>3}{1:0>3}{2:0>3}%".format(r, g, b));
      else:

        r = self.limit_node_bright(colors[0])
        g = self.limit_node_bright(colors[1])
        b = self.limit_node_bright(colors[2])

        serial_array.append("{0:0>3}{1:0>3}{2:0>3}{3:0>3}".format(x, r, g, b))

    serial_array.append(self.END_CHAR)

    output.write("".join(serial_array))

    self.frame_delay()

  def set_node(self, pos, color=[0, 0, 0]):
    self.frame[pos] = color

  def set_frame(self, frame_array):
    # warning: can fuck shit up right here
    self.frame = np.asarray(frame_array, dtype=np.uint8)

  def limit_node_bright(self, val):
    return int(val * self.NODE_BRIGHTNESS)

  def limit_spire_bright(self, val):
    return int(val * self.SPIRE_BRIGHTNESS)

  def frame_delay(self):
    time.sleep(self.FRAME_DELAY)

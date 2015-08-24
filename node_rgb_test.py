from zoo import Zoo
from time import sleep

z = Zoo()

while True:

  for x in range(z.NODE_COUNT):

    z.set_node(x, [255, 0, 0])
    z.send_frame()

    sleep(.1)

    z.set_node(x, [0, 255, 0])
    z.send_frame()

    sleep(.1)

    z.set_node(x, [0, 0, 255])
    z.send_frame()

    sleep(.1)

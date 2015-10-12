from zoo import Zoo
import atexit

z = Zoo()

def cleanup():
  z.reset_frame()
  z.send_frame()

atexit.register(cleanup)

while True:
  pos = raw_input("Position (0-"+str(z.NODE_COUNT-1)+" or 'all'): ")
  r = int(raw_input("Red: "))
  g = int(raw_input("Green: "))
  b = int(raw_input("Blue: "))

  print pos, r, g, b
  z.reset_frame()

  if pos.lower() == 'all':
    for i in range(z.NODE_COUNT):
      z.set_node(i, [r, g, b])
  else:
    z.set_node(int(pos), [r, g, b])

  z.send_frame()


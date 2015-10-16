from zoo import Zoo
import atexit

z = Zoo()

def cleanup():
  z.reset_frame()
  z.send_frame()

atexit.register(cleanup)

def color_prompt():
  r = int(raw_input("Red: "))
  g = int(raw_input("Green: "))
  b = int(raw_input("Blue: "))
  return (r, g, b)

r, g, b = color_prompt()

while True:
  pos = raw_input("Position (0-"+str(z.NODE_COUNT-1)+"), or 'all', or 'c' to set a new color: ")

  if pos.lower() == 'c':
    r, g, b = color_prompt()
    pos = raw_input("Position (0-"+str(z.NODE_COUNT-1)+"), or 'all': ")

  print pos, r, g, b

  z.reset_frame()

  if pos.lower() == 'all':
    for i in range(z.NODE_COUNT):
      z.set_node(i, [r, g, b])
  else:
    z.set_node(int(pos), [r, g, b])

  z.send_frame()


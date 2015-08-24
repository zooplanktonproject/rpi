from zoo import Zoo
import atexit

z = Zoo()

def cleanup():
  z.reset_frame()
  z.send_frame()

atexit.register(cleanup)

while True:
  pos = int(raw_input("Position: "))
  r = int(raw_input("Red: "))
  g = int(raw_input("Green: "))
  b = int(raw_input("Blue: "))

  print pos, r, g, b
  z.reset_frame()
  z.set_node(pos, [r, g, b])
  z.send_frame()


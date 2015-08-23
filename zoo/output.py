from sys import platform as _platform

# write to serial unless on osx
def write(str):
  if _platform == "darwin":
    print str
  else:
    write_serial(str)

def write_serial(str):
  import serial
  ser = serial.Serial('/dev/ttyACM0', 9600)
  ser.write(str)

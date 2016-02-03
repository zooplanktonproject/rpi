from sys import platform as _platform
import socket
import json

with open('./config/conf.json') as data_file:
  conf = json.load(data_file)

output = conf["output"]

if output == "udp":

  UDP_IP = conf["udp"]["ip"]
  UDP_PORT = conf["udp"]["port"]

  sock = socket.socket(socket.AF_INET, # Internet
                       socket.SOCK_DGRAM) # UDP

def write(str):
  if output == "console":
    print str
  elif output == "serial":
    write_serial(str)
  elif output == "udp":
    write_udp(str)

def write_serial(str):
  import serial
  ser = serial.Serial('/dev/ttyACM0', 9600)
  ser.write(str)

def write_udp(str):
  sock.sendto(str, (UDP_IP, UDP_PORT))

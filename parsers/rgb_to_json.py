import json
from PIL import Image
from os import listdir
from os.path import isfile, join

mypath = "./data/gifs"

onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

with open('./config/nodes.json') as data_file:
    nodes = json.load(data_file)

for filename in onlyfiles:
  if filename.endswith(".gif"):
    print filename
  else:
    print filename + " is not a gif!"
    continue

  # empty fucker
  ordered_nodes = [None] * len(nodes)

  # populate fucker
  for i, pos in nodes.items():
    ordered_nodes[int(i)] = [pos['x'], pos['y']]

  im = Image.open("./data/gifs/"+filename) #Can be many different formats.

  target_size = 400, 400

  print im.size

  resize = False
  if im.size != target_size:
    print "RESIZE"
    resize = True

  data = []

  # To iterate through the entire gif
  try:
    frame_num = 0
    while True:
      im.seek(frame_num)

      frame_data = []

      # do something to im
      img = im.convert('RGB')

      if resize == True:
        #print "Resizing", im.size, target_size
        img = img.resize(target_size, Image.ANTIALIAS)

      for x, y in ordered_nodes:
        frame_data.append(img.getpixel((x, y)))

      #print r, g, b
      data.append(frame_data)

      #print frame_num
      frame_num+=1
  except EOFError:
      pass # end of sequence


  with open("./data/frames/" + filename[:filename.index('.gif')] + ".json", 'w') as outfile:
      json.dump({
        "meta": {},
        "data": data
      }, outfile)


  #print im.size #Get the width and hight of the image for iterating over
  #print pix[,y] #Get the RGBA Value of the a pixel of an image

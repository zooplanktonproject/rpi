import json
from PIL import Image, ImageFont, ImageDraw

with open('./config/nodes.json') as data_file:
    data = json.load(data_file)


gray = (200, 200, 200)
black = (0,0,0)
lightblue = (225, 255, 255)
darkblue = (185, 255, 255)

img = Image.new("RGBA", (400,400), 128)

usr_font = ImageFont.truetype("./fonts/Arial.ttf", 10)

draw = ImageDraw.Draw(img)

# grid
for i in range(10, 400, 10):

  if (i / 50.0) % 1 == 0:
    fillcolor = darkblue
  else:
    fillcolor = lightblue

  draw.line([(i, 1), (i, 399)], fill=fillcolor, width=1)
  draw.line([(1, i), (399, i)], fill=fillcolor, width=1)


# square border
draw.line([
  (1, 1), (1, img.size[1]-1),
  (1, img.size[1]-1), (img.size[0]-1, img.size[1]-1),
  (img.size[0]-1, img.size[1]-1), (img.size[0]-1, 1),
  (img.size[0]-1, 1), (1, 1)
  ], fill=gray, width=1)

# crosshair
draw.line([(img.size[0]/2, 1), (img.size[0]/2, img.size[1]-1)], fill=gray, width=1)
draw.line([(1, img.size[1]/2), (img.size[0]-1, img.size[1]/2)], fill=gray, width=1)


# top tier circle approximation
draw.ellipse([
  (130, 130),
  (270, 270)
  ], fill=None, outline=black)

# roof tier approximation
draw.ellipse([
  (60, 60),
  (340, 340)
  ], fill=None, outline=black)

# bottom tier (walls) approximation
draw.ellipse([
  (25, 25),
  (375, 375)
  ], fill=None, outline=black)


# label the global position numbers
for i, pos in data.items():
  # -pos['y'] + 400 if you want to flip the y axis
  draw.point((pos['x'], pos['y']), (0, 0, 0))
  draw.text((pos['x'], pos['y']), i, (0,0,0), font=usr_font)

img.save("./data/positions.png", "PNG")

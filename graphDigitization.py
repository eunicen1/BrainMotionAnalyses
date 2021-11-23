from PIL import Image
import csv
def digitize(imagenm, newname = '', color = (0,0,0), initx = -0.8, inity = -0.8, endx = 0.4, endy = 0.6):
 if(newname == ''):
  newname = imagenm
 im = Image.open(imagenm)
 rgb_im = im.convert('RGB')
 width = int(rgb_im.size[0])
 height = int(rgb_im.size[1])
 dx = endx - initx
 dy = endy - inity
 f = open(newname+".csv", 'w', newline = "")
 for y in range(height):
  actualy = endy - y*dy/(height)
 for x in range(width):
  actualx = initx + x*dx/(width)
 r, g, b = rgb_im.getpixel((x, y))
 if (r,g,b) == color:
  print(f"Found {color} at scaled {actualx},{actualy}!")
 writer = csv.writer(f, delimiter = ",")
 writer.writerow([color, actualx, actualy])

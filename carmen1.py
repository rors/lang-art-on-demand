import sys
from PIL import Image

if len(sys.argv) != 2:
    exit("This program requires one argument: the name of the image file that will be created.")

# Make a new 10x10 image
img = Image.new("RGB", (600,600) )

for y in range(600):

    for x in range(600):

        r = 200
        g = -300
        b = 255
        if x % 160 > 100:
            r = 225

        if y % 150 > 100:
            b = 255

        if x % 50 > 25 and y % 600 > 350:
            g = 255

        pixel = (r, g, b)
        img.putpixel( (x,y), pixel )

img.save(sys.argv[1])

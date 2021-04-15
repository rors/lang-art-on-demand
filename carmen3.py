import sys
from PIL import Image

if len(sys.argv) != 2:
    exit("This program requires one argument: the name of the image file that will be created.")

# Make a new 400x400 image
img = Image.new("RGB", (400,400) )

for y in range(400):

    for x in range(400):

        r = 0
        g = 80
        b = 100
        if x % 100 > 25:
            r = 200

        if y % 200 > 100:
            b = 255

        if x % 100 > 50 and y % 100 > 50:
            g = 255

        pixel = (r, g, b)
        img.putpixel( (x,y), pixel )

img.save(sys.argv[1])

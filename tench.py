import sys
from PIL import Image

if len(sys.argv) != 2:
    exit("This program requires one argument: the name of the image file that will be created.")

# Make a new 400x400 image
img = Image.new("RGB", (400,400) )

for y in range(400):

    for x in range(400):

        r = 0
        g = 0
        b = 0
        if x % 50 > 25:
            r = x % 100

        if y % 50 > 25:
            b = round(y/2)

        if x % 100 > 50 and y % 100 > 50:
            g = x

        pixel = (r, g, b)
        img.putpixel( (x,y), pixel )

img.save(sys.argv[1])

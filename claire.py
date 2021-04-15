import sys
from PIL import Image

if len(sys.argv) != 2:
    exit("This program requires one argument: the name of the image file that will be created.")

# Make a new 400x400 image
img = Image.new("RGB", (400,400) )


for y in range(400):

    for x in range(400):

        r = 111
        g = 252
        b = 3
        if x % 100 == 1:
            r = 13
            g = 24
            b = 168

        if y % 10 > x:
            r = 255
            g = 255
            b = 255



        pixel = (r, g, b)
        img.putpixel( (x,y), pixel )

img.save(sys.argv[1])

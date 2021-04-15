#note to self - in Terminal, use python3 with PIL

import sys
from PIL import Image

if len(sys.argv) != 2:
    exit("This program requires one argument: the name of the image file that will be created.")

# Make a new 400x400 image
img = Image.new("RGB", (400,400) )

for y in range(400):

    for x in range(400):

        r = 0
        g = 100
        b = 0
        if x % 30 > 5:
            r = 255

        if y % 50 < x:
            b = 255

        if x % 50 > 40 and y % 20 > 10:
            g = 255

        pixel = (r, g, b)
        img.putpixel( (x,y), pixel )

img.save(sys.argv[1])

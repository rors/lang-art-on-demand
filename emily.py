import sys
from PIL import Image

if len(sys.argv) != 2:
    exit("This program requires one argument: the name of the image file that will be created.")

# Make a new 10x10 image
img = Image.new("RGB", (400,400) )

for y in range(400):

    for x in range(400):

        r = 0
        g = 0
        b = 0

        if y % 160 > 8:
            r = 228
            g = 0
            b = 43

        if x % 166 > 20 and y % 155 > 15:
            r = 0
            g = 61
            b = 165

        if x % 180 < 80:
            r = 245
            g = 223
            b = 77

        if x % 300 < 20:
            r = 0
            g = 0
            b = 0

        if y % 300 < 10:
            r = 0
            g = 0
            b = 0

        pixel = (r, g, b)
        img.putpixel( (x,y), pixel )

img.save(sys.argv[1])

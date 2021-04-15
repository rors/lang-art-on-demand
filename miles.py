import sys
from PIL import Image

if len(sys.argv) != 2:
    exit("This program requires one argument: the name of the image file that will be created.")

# Make a new 400x400 image
img = Image.new("RGB", (400,400) )

for y in range(400):

    for x in range(400):

        pixel = (x % 255, 0, y % 255)
        img.putpixel( (x,y), pixel )

img.save(sys.argv[1])

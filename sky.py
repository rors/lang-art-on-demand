import sys
from PIL import Image

if len(sys.argv) != 2:
    exit("This program requires one argument: the name of the image file that will be created.")

# Make a new 600x400 image
img = Image.new("RGB", (600,400) )

# Import color in each pixel by order, not grid
data = []
for i in range(600):
    for j in range(400):
        # On these occasions, add green strikes
        if i % 100 == 0 or i %70 == 0:
            g = 255
        else:
            g = 0

        if j%100 ==0:
            g = 200

        pixel = (i%255, g, j%255)
        data.append( pixel )

img.putdata(data)

img.save(sys.argv[1])
print("Done producing img!")

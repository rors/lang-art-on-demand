
# This code was modified from Carmen Huang's
# Unit 1, Exercise 3 work from Code as a Liberal Art, Spring 2021
#
# originally carmen3.py in this repo.
# 
# These adaptations were made as a collaboration between Miranda Elder (@mirandaelder)
# and Rory Solomon (@rors)

import sys
from PIL import Image

if len(sys.argv) != 6:
    exit("This program requires 6 arguments: the name of the image file that will be created and 4 numbers.")

# Make a new 400x400 image
img = Image.new("RGB", (400,400) )

p = []
for i in sys.argv[2:6]:
    if i.isnumeric():
        p.append( int(i) )
    else:
        sum = 0
        for char in i:
            sum = sum + ord(char)
        p.append(int(sum))

# Normalize the params
p = [ i/max(p) for i in p ]

print(p)

l = len(sys.argv[1])
print(l)

for y in range(400):

    for x in range(400):

        r = round(p[0]*255) + l
        g = round(p[0]*255) - l
        b = round(p[0]*255)

        if x % round(50+100*p[1]) > 10+l:
            r = round(p[1]*255)

        if y % round(150+100*p[3]) > 50+l:
            b = round(p[3]*255)

        if x % round(5+50*p[2]) > l and y % round(5+50*p[2]) > l:
            g = round(p[2]*255)

        pixel = (r, g, b)
        img.putpixel( (x,y), pixel )

img.save(sys.argv[1]+".png")

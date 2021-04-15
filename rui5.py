import sys
from PIL import Image

if len(sys.argv) != 3:
    exit("This program requires two arguments: the name of two image files to combine.")


# open both images
img1 = Image.open( sys.argv[1] )
img2 = Image.open( sys.argv[2] )

# resize both images so they are no bigger than 400x400
# but preserve the original aspect ratio
img1.thumbnail( (400,400) )
img2.thumbnail( (400,400) )

# make a new image 600x600, with a white background
# Note that this image now has an "alpha" component
new_image = Image.new( "RGBA", (600,600), "white" )

# paste in the first image to the upper-left corner (0,0)
new_image.paste(img1, (0,0) )

# convert the second image to a new image with transparency (alpha)
img2_alpha = img2.convert("RGBA")

# modify the second image, make all bluish pixels totally transparent
# (alpha 255)
(width,height) = img2_alpha.size
for x in range(width):
    for y in range(height):
        (red,green,blue) = img2_alpha.getpixel((x,y))
        if blue > red and blue > green:
            img2_alpha.putpixel( (x,y), (0,0,0,0) )


# paste in the second image, preserving its new transparency.
# Note that this time I'm placing it at 0,0 to show the transparent overlay
new_image.alpha_composite(img2_alpha, (0,0) )

# save the resulting image
# Note that we must convert it to RGB with no alpha to save it as a JPEG
new_image.convert("RGB").save("new.jpg")

# Alternatively, we could have avoided converting by saving it to a
# PNG like this (since PNGs allow alpha):
# new_image.save("new.png")

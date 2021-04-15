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
new_image = Image.new( "RGB", (600,600), "white" )

# paste in the first image to the upper-left corner (0,0)
new_image.paste(img1, (0,0) )

# paste in the second image, to (200,200)
new_image.paste(img2, (200,200) )

# save the resulting image
new_image.save("example6.jpg")

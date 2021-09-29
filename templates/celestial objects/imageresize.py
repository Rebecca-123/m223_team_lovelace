from PIL import Image

def image_resize():

    im = Image.open("/static/assets/mercury_no_bg.png")

    #Make the new image half the width and half the height of the original image
    resized_im = im.resize((round(im.size[0]*5), round(im.size[1]*5)))

    #Display the resized imaged
    resized_im.show()
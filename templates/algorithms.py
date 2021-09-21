from PIL import Image, ImageDraw

img = Image.open('/static/assets/solarsystem_stego.jpg')

draw = ImageDraw.Draw(img)
draw.text((30, 60), "This is a test!", fill=(223,223,223))
img.show()
img.save("static/assets/new_solarsystem_stego.jpg")
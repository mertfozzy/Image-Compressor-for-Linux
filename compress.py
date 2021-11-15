import PIL
from PIL import Image

mywidth = 4032

img = Image.open('/home/mert/Desktop/Image-Compressor-for-Linux/test.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save('/home/mert/Desktop/Image-Compressor-for-Linux/resized.jpg')
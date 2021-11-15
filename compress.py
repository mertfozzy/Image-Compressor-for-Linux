import PIL
from PIL import Image
import os

mywidth = 4032
source_dir = "/home/mert/Desktop/Image-Compressor-for-Linux/source"
destination_dir = "/home/mert/Desktop/Image-Compressor-for-Linux/destination"

def resize_pic(old_pic, new_pic, mywidth):
    img = Image.open(old_pic)
    wpercent = (mywidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
    img.save(new_pic)

def entire_directory(sour_dir, dest_dir, width):
    files = os.listdir(sour_dir)

    i = 0
    for file in files:
        i += 1

        old_pic_dir = sour_dir + "/" + file
        new_pic_dir  = dest_dir + "/" + file

        resize_pic(old_pic_dir , new_pic_dir, width)
        print(i, "done")

        #print("old pic : ", old_pic_dir )
        #print("new pic : ", new_pic_dir )


    #print(files)

entire_directory(source_dir, destination_dir, mywidth)
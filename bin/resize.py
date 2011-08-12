import Image
import os
from time import mktime
from stat import *

def resize(filename):
    name, ext = os.path.splitext(filename)

    image = Image.open(filename)

    w, h = image.size
    width = 200
    height = int( float(width)/float(w) * float(h) )
    print w,h,width,height

    name = name + "_low_res.jpg"
    shunken = image.resize((width, height), Image.ANTIALIAS)
    shunken.save(name)

if __name__ == '__main__':
    resize("1000.jpg")

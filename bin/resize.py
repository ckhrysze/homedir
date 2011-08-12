#!/usr/bin/env python

import Image
import os
import sys
from time import mktime
from stat import *

def resize(filename):
    name, ext = os.path.splitext(filename)

    image = Image.open(filename)

    w, h = image.size
    width = 250
    height = int( float(width)/float(w) * float(h) )

    name = name + "_low_res.jpg"
    print "Resized to file %s" % name
    shunken = image.resize((width, height), Image.ANTIALIAS)
    shunken.save(name)

if __name__ == '__main__':
    resize(sys.argv[1])

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 04:22:31 2017

@author: heisenberg
"""

from PIL import Image
import numpy

img_left = Image.open("/home/heisenberg/Desktop/Anaglyph_project/img4_left.png")
img_right = Image.open("/home/heisenberg/Desktop/Anaglyph_project/img4_right.png")

#base_height = 384
#base_width = 576

#img_left = img_left.resize((base_width,base_height),Image.ANTIALIAS)
#img_right = img_right.resize((base_width,base_height),Image.ANTIALIAS)

crop_left = 100
crop_right = 100

img_left = img_left.crop((crop_left,0,img_left.size[0],img_left.size[1]))
img_right = img_right.crop((0,0,img_right.size[0]-crop_right,img_right.size[1]))

Image_map = {
    'map_1': [ [ 1, 0, 0, 0, 0, 0, 0, 0, 0 ], [ 0, 0, 0, 0, 1, 0, 0, 0, 1 ] ],
}





def anaglyph(left, right, path):
    width, height = left.size
    leftMap = left.load()
    rightMap = right.load()
    m = Image_map['map_1']

    for y in range(0, height):
        for x in range(0, width):
            r1, g1, b1 = leftMap[x, y]
            r2, g2, b2 = rightMap[x, y]
#            leftMap = ImageChops.screen(img_left,img_right)
            leftMap[x, y] = (
                int(r1*m[0][0] + g1*m[0][1] + b1*m[0][2] + r2*m[1][0] + g2*m[1][1] + b2*m[1][2]),
                int(r1*m[0][3] + g1*m[0][4] + b1*m[0][5] + r2*m[1][3] + g2*m[1][4] + b2*m[1][5]),
                int(r1*m[0][6] + g1*m[0][7] + b1*m[0][8] + r2*m[1][6] + g2*m[1][7] + b2*m[1][8])
            )
    left.save(path)

anaglyph(img_left, img_right, "/home/heisenberg/Desktop/Anaglyph_project/img4_anaglyph_cropped_150.jpg")

#image = 

anaglyphed_img = Image.open("/home/heisenberg/Desktop/Anaglyph_project/img4_anaglyph.jpg")
anaglyphed_csuf = Image.open("/home/heisenberg/Desktop/Anaglyph_project/cal_state_anaglyphed.png")
#data_csuf = numpy.asarray(anaglyphed_csuf)
#data_img = numpy.asarray(anaglyphed_img)
#
#for i in range(0,29):
#    for j in range(0,100):
#        for k in range(0,3):
#            data_img[356+i][477+j][k] = data_csuf[j][i][k]
#anaglyphed_img.paste(anaglyphed_csuf,(anaglyphed_img.size[0]-549,anaglyphed_img.size[1]-171),anaglyphed_csuf)
a,b = anaglyphed_csuf.size
anaglyphed_img.paste(anaglyphed_csuf,(0,0),anaglyphed_csuf)
anaglyphed_img.save("/home/heisenberg/Desktop/Anaglyph_project/img4_anaglyph_with_logo.jpg")

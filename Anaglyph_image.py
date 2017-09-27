#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 04:22:31 2017

@author: heisenberg
"""

from PIL import Image,ImageChops
import numpy

def anaglyph_2d_3d(img1,shift):
    width, height = img1.size
    
    img_left = img1
    img_left = numpy.array(img_left)
    img_right = img1
    img_right = numpy.array(img_right)
    
    img_left[:,:,1] *= 0
    img_left[:,:,2] *= 0
    
    img_right[:,:,0] *= 0
    
    final_image = numpy.zeros((height,width+shift,3),'uint8')
    
    for i in range(0,width):
        for j in range(0,height):
            final_image[j,i,0] = img_left[j,i,0]
            final_image[j,i+shift,1] = img_right[j,i,1]
            final_image[j,i+shift,2] = img_right[j,i,2]
    img = Image.fromarray(final_image)
    return img

def anaglyph_from_stereo_images(left, right, path, crop_size):
    width, height = left.size
    
    left = left.crop((crop_size,0,left.size[0],left.size[1]))
    right = right.crop((0,0,right.size[0]-crop_size,right.size[1]))
    
    left = numpy.array(left)
    right = numpy.array(right)
    
    left[:,:,1] *= 0
    left[:,:,2] *= 0
        
    right[:,:,0] *= 0
    
    left = Image.fromarray(left)
    right = Image.fromarray(right)
    
    img = ImageChops.screen(left,right)
    return img


img_left = Image.open("/home/heisenberg/Desktop/Anaglyph_project/img4_left.png")
img_right = Image.open("/home/heisenberg/Desktop/Anaglyph_project/img4_right.png")

anaglyph_object_image = anaglyph_from_stereo_images(img_left, img_right, "/home/heisenberg/Desktop/Anaglyph_project/img4_anaglyph_cropped_150.jpg",100)

anaglyph_logo = anaglyph_2d_3d(Image.open("/home/heisenberg/Desktop/Anaglyph_project/orange_county_girls_scout.jpg"),15)

anaglyph_object_image.paste(anaglyph_logo,(0,0))

anaglyph_object_image.save("/home/heisenberg/Desktop/Anaglyph_project/img4_anaglyph_with_logo.jpg")

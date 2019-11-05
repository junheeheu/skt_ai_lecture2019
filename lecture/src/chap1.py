# -*- coding: utf-8 -*-
"""
@file chap1.py
@brief image load by opencv
@author Jun-Hee HEU
@contact junhee.heu@sk.com
@data 2019.11.05
"""

import cv2
import os
import pdb

print('--------- Chap. 1. Load Image using OpenCV ---------')

imgpath = '../../../junface.jpg'
savepath = '../../../save_junface.jpg'

img = cv2.imread(imgpath)
cv2.imwrite(savepath, img)


print('--------- Go To Next Chapter ---------')
# -*- coding: utf-8 -*-
"""
@file chap3.py
@brief register faces
@author Jun-Hee HEU
@contact junhee.heu@sk.com
@data 2019.11.05
"""

from api_util import sktface
import os

print('--------- Step. 2. Register your face in your namespace ---------')

imgroot = '../../../enrol'

skt = sktface(name)

imglist = os.listdir(imgroot)

for imgname in imglist:
    imgpath = '%s/%s' % (imgroot, imgname)
    skt.register_face(imgpath)

print('--------- Go To Next Chapter ---------')
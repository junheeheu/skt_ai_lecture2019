# -*- coding: utf-8 -*-
"""
@file chap3.py
@brief test identification
@author Jun-Hee HEU
@contact junhee.heu@sk.com
@data 2019.11.05
"""

from api_util import sktface
import os

print('--------- Step. 3. Identify a face ---------')

imgroot = '../../../test'
name = 'junhee'

skt = sktface(name)

imglist = os.listdir(imgroot)

for imgname in imglist:
    imgpath = '%s/%s' % (imgroot, imgname)
    if not os.path.exists(imgpath):
        print('check the path')
    skt.identify(imgpath)

print('--------- Go To Next Chapter ---------')
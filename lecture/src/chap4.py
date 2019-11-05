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
import cv2

print('--------- Step. 3. Identify a face ---------')

imgroot = '../../../test'
name = 'junhee'

skt = sktface(name)

imglist = os.listdir(imgroot)

for imgname in imglist:
    imgpath = '%s/%s' % (imgroot, imgname)
    if not os.path.exists(imgpath):
        print('check the path')
    results = skt.identify(imgpath)
    img = cv2.imread('%s/%s' % (imgroot, imgname))
    sx = results['face_box']['topLeftX']
    sy = results['face_box']['topLeftY']
    ex = sx + results['face_box']['faceWidth']
    ey = sy + results['face_box']['faceHeight']
    cv2.rectangle(img, (sx,sy), (ex,ey), (0,255,255), 5)
    txt = 'name: %s, %s, %d, %s' % (results['subject_name'], results['gender'], results['age'], results['expression'])
    cv2.putText(img, txt, (sx + 10, sy+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,255), 1)

    cv2.imwrite('testresult.jpg', img)

print('--------- Go To Next Chapter ---------')
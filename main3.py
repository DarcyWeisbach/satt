#!/usr/bin/env python
        # -*- coding: utf-8 -*-
import time
import picamera
import numpy as np
import random
import sys
import cv2
from color1 import RedDetect
from ai import Qlearning
import motor2
camera = picamera.PiCamera()
camera.resolution=(600,600)
def imageProcessing(a):
    image = cv2.GaussianBlur(a,(5,5),0)
    mono_src = RedDetect.red_detect(image)
    label = cv2.connectedComponentsWithStats(mono_src)
    return label

def Menseki(a):
    a1 = a[(a>=0) & (a<120)]
    a1 = np.sum(a1)
    a2 = a[(a>=120) & (a<240)]
    a2 = np.sum(a2)
    a3 = a[(a>=240) & (a<=360)]
    a3 = np.sum(a3)
    a4 = a[(a>360) & (a<=480)]
    a4 = np.sum(a4)
    a5 = a[(a>480) & (a<=600)]
    a5 = np.sum(a5)
    return np.array([a1,a2,a3,a4,a5])



def main():
    for i in range(10):
        start=time.time()
        camera.capture('test1.png')
        image1 = cv2.imread('./test1.png')
        label=np.array(imageProcessing(image1))
        n = label[0] - 1
        data = np.delete(label[2], 0, 0)
        center = np.delete(label[3], 0, 0)
        menseki=Menseki(data)
        fin=time.time()-start
        print(s)
        print(fin)
        sum = np.sum(s)
        if sum >200:
            max_surface_area = np.argmax(s)
            motor2.Motor(max_surface_area)
            motor2.breake()
        else:
            motor2.go(1)
            motor2.right(2)"""回転"""
            motor2.breake()
if __name__ == '__main__':
    main()

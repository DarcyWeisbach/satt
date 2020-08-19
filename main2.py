#!/usr/bin/env python
        # -*- coding: utf-8 -*-
import time
import picamera
import numpy as np
import random
import sys
import cv2
from color1 import RedDetect
from ai1 import satt
import motor2
camera = picamera.PiCamera()
camera.resolution=(600,600)
def imageProcessing(a):
    image = cv2.GaussianBlur(a,(5,5),0)
    mono_src = RedDetect.red_detect(image)
    label = cv2.connectedComponentsWithStats(mono_src)
    return label

def main():
    for i in range(10):
        start=time.time()"""時間計測"""
        camera.capture('test1.png')
        image1 = cv2.imread('./test1.png')
        label=imageProcessing(image1)
        n = label[0] - 1
        data = np.delete(label[2], 0, 0)
        center = np.delete(label[3], 0, 0)
        s = Qlearning.discretization(center,data,n)
        fin=time.time()-start
        print(s)
        print(fin)
        """add !!! 面積の合計が小さければモーター処理を行わない"""
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

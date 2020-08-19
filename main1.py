#!/usr/bin/env python
        # -*- coding: utf-8 -*-
import time
import picamera #taking pictures is faster than opencv
import numpy as np
import random
import sys
import cv2#processing pictures is fastet than picamera
from color import RedDetect
from ai1 import satt
import motor

def main():
    camera = picamera.PiCamera()
    camera.resolution=(600,600)
    #for the moment,we do 50 trials
    #for loop is fast
    for i in range(50):
        camera.capture('test1.png')#take picture
        image1 = cv2.imread('./test1.png')
        image = cv2.GaussianBlur(image1,(5,5),0)#delete white noise
        mono_src = RedDetect.red_detect(image)
        # ラベリング処理
        label = cv2.connectedComponentsWithStats(mono_src) #make array to get imformation
        '''connectedComponentsWithStats
        0:the number of image , 1:image with labels, 2:center'''
        if label:
            # オブジェクト情報を項目別に抽出
            n = label[0] - 1
            data = np.delete(label[2], 0, 0)
            center = np.delete(label[3], 0, 0)
            '''delete is to delete black labels  0 is black flame, so first square is number 1,second square is number 2
            0 is not needed, so I want to delete black flame of number 0
            '''
            s = Qlearning.discretization(center,data,n)
            print(s)
            #配列の最も大きい値のkeyかlabelを返す関数
            max_surface_area = np.argmax(s)
            #get upfunc ,そこにモータの動きをさせる
            motor.Motor(max_surface_area)
        else:
            print("0")
            continue
if __name__ == '__main__':
    main()

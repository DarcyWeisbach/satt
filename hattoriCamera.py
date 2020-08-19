#!/usr/bin/env python
        # -*- coding: utf-8 -*-

import time
import picamera
import numpy as np
import random
import sys
import cv2


def red_detect(img):
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    hsv_min = np.array([0,127,0])
    hsv_max = np.array([30,127,0])
    mask1 = cv2.inRange(hsv, hsv_min, hsv_max)

    hsv_min = np.array([150,127,0])
    hsv_max = np.array([179,255,255])
    mask2 = cv2.inRange(hsv, hsv_min, hsv_max)

    return mask1 + mask2

def discretization(array1,array2,number):
    area = [0,0,0,0,0]
    for i in range(number):
        if 0<=array1[i][1]<120:
            area[0]+=array2[i][4]
        if 120<=array1[i][1]<240:
            area[1]+=array2[i][4]
        if 240<=array1[i][1]<=360:
            area[2]+=array2[i][4]
        if 360<array1[i][1]<=480:
            area[3]+=array2[i][4]
        if 480<array1[i][1]<=600:
            area[4]+=array2[i][4]

    return area




def main():
    camera = picamera.PiCamera()
    camera.resolution=(600,600)
    while True:
        camera.capture('test1.png')#take picture
        image1 = cv2.imread('./test1.png')
        image = cv2.GaussianBlur(image1,(5,5),0)#delete white noise
        mono_src=red_detect(image)
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
            0 is not needed, so i want to delete black flame of number 0
            '''
            s=discretization(center,data,n)
            print(s)


        else:
            print("0")
            continue
if __name__ == '__main__':
    main()

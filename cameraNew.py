#!/usr/bin/env python
        # -*- coding: utf-8 -*-

import time
import picamera
import numpy as np
import random
import sys
import cv2
import time

def red_detect(img):
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    hsv_min = np.array([0,127,0])
    hsv_max = np.array([30,127,0])
    mask1 = cv2.inRange(hsv, hsv_min, hsv_max)

    hsv_min = np.array([150,127,0])
    hsv_max = np.array([179,255,255])
    mask2 = cv2.inRange(hsv, hsv_min, hsv_max)

    return mask1 + mask2



def main():
    camera = picamera.PiCamera()
    camera.resolution=(600,600)
    while True:
        #camera = picamera.PiCamera()
        #camera.resolution=(600,600)
        #camera.hflip=True
        #camera.vflip=True
        camera.capture('test1.jpeg')

        image1 = cv2.imread('./test1.jpeg')
        image = cv2.GaussianBlur(image1,(5,5),0)#delete white noise
        #mask = red_detect(image)
        mono_src=red_detect(image)
        #cv2.imshow('RED_DETECT',mask)
        cv2.imshow('RED_DETECT',mono_src)

            # 画像をグレースケールで読み込み
        #gray_src = cv2.imread('test1.png', 0)

            # 前処理（平準化フィルターを適用した場合）
            # 前処理が不要な場合は下記行をコメントアウト
        #blur_src = cv2.GaussianBlur(gray_src, (5, 5), 2)

            # 二値変換
            # 前処理を使用しなかった場合は、blur_srcではなくgray_srcに書き換えるする
        #mono_src = cv2.threshold(blur_src, 48, 255, cv2.THRESH_BINARY_INV)[1]

            # ラベリング結果書き出し用に二値画像をカラー変換
        color_src01 = cv2.cvtColor(mono_src, cv2.COLOR_GRAY2BGR)
        color_src02 = cv2.cvtColor(mono_src, cv2.COLOR_GRAY2BGR)


            # ラベリング処理
        label = cv2.connectedComponentsWithStats(mono_src) #make array to get imformation
        '''connectedComponentsWithStats
        0:the number of image , 1:image with labels, 2:center'''
        time.sleep(1)
        if label:
            n = label[0] - 1
            data = np.delete(label[2], 0, 0)
            center = np.delete(label[3], 0, 0)
            print(label[3])
        time.sleep(2)
    '''delete is to delete black labels  0 is black flame, so first square is number 1,second square is number 2
       0 is not needed, so i want to delete black flame of number 0'''
'''
            # オブジェクト情報を利用してラベリング結果を画面に表示
    for i in range(n):

                # 各オブジェクトの外接矩形を赤枠で表示
        x0 = data[i][0]
        y0 = data[i][1]
        x1 = data[i][0] + data[i][2]
        y1 = data[i][1] + data[i][3]
        cv2.rectangle(color_src01, (x0, y0), (x1, y1), (0, 0, 255))
        cv2.rectangle(color_src02, (x0, y0), (x1, y1), (0, 0, 255))

                # 各オブジェクトのラベル番号と面積に黄文字で表示
        cv2.putText(color_src01, "ID: " +str(i + 1), (x1 - 20, y1 + 15), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255))
        cv2.putText(color_src01, "S: " +str(data[i][4]), (x1 - 20, y1 + 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255))

                # 各オブジェクトの重心座標をに黄文字で表示
        cv2.putText(color_src02, "X: " + str(int(center[i][0])), (x1 - 30, y1 + 15), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255))
        cv2.putText(color_src02, "Y: " + str(int(center[i][1])), (x1 - 30, y1 + 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255))
'''
        # 結果の表示
        #cv2.imshow("color_src01", color_src01)
        #cv2.imshow("color_src02", color_src02)
        #print(label[2])
        #print(label[3])
        #cv2.destroyAllWindow

if __name__ == '__main__':
    main()

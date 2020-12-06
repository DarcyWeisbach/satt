# !/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import picamera
import numpy as np
#import random
import sys
import cv2
"""
この関数はカメラ撮影とバイナリ化（二値化処理）した画像の配列を返すものです．
確認し忘れていましたが，0 or 255　のデータです．
面積の求め方はnonzeroを使う方法です．
255を1にする方法もあるのでそちらでも良いです・

引数はいりません．返り値として二値化した配列とtrue　or falseを返します．
"""

def red_detect(img):
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    hsv_min = np.array([0,55,80])
    hsv_max = np.array([5,255,255])
    mask1 = cv2.inRange(hsv, hsv_min, hsv_max)

    hsv_min = np.array([160,110,80])
    hsv_max = np.array([180,255,255])
    mask2 = cv2.inRange(hsv, hsv_min, hsv_max)
    return mask1 + mask2


def capture():
    #初期設定なので関数内に入れる必要はないです．
    camera=picamera.PiCamera()
    camera.resolution(1200,1200)
    #ここから関数

    """
    引数のところに保存する名前を入れてください
    関数内でループをさせていないので，写真を保存するのであれば名前を変える必要があります．
    私が良くやるのはループの回数を名前にする方法です．
    "./"+src(i)+".jpg"などです．
    """
    camera.capture("./a.jpg")
    #保存した画像の読み込みです．保存しない方が早いかもしれないので変更してもよいかも
    image1=cv2.imread("./a.jpg")
    #ノイズ処理です．ただ，csvが割と感度が良いのでいらないかもしれないです．
    image1 = cv2.GaussianBlur(image1, (5, 5), 3)  
    #別に定義された関数を用いています．やろうと思えば一つの関数になると思いますが高級関数的な使い方になるのでやめました．
    mono_src = red_detect(image1)
    #0じゃない値の数を数えます．（結局面積を求めていることと同じ．単位はピクセル）
    num = np.count_nonzero(mono_src)

    return mono_src

        
if __name__ == '__main__':
    capture()
    print("finish")


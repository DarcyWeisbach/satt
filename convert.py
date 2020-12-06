# -*- coding: utf-8 -*-
import cv2
import numpy as np

def convert(array,theta,scale=1.0):
    h,w=array.shape
    array_pad = np.pad(array, ((int(0.2*h), int(0.2*h)),(int(0.2*w), int(0.2*w))), 'constant')
    oy, ox = int(array_pad.shape[0]/2), int(array_pad.shape[1]/2)
    R = cv2.getRotationMatrix2D((ox, oy), theta, scale)  
    dst = cv2.warpAffine(array_pad, R, (w, h))    # アフィン変換
    cv2.imwrite("./b.jpg", dst)
    array_sum = dst.sum(axis=0)
    array_divide = np.array_split(array_sum,5)
    array_select = np.array([np.sum(array_divide[i]) for i in range(5)])
    array_index = array_select.index(max(array_select))
    print array_index/5







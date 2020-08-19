#!/usr/bin/env python
        # -*- coding: utf-8 -*-
import cv2
import numpy as np
class RedDetect:
    def red_detect(img):
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        hsv_min = np.array([0,127,0])
        hsv_max = np.array([30,127,0])
        mask1 = cv2.inRange(hsv, hsv_min, hsv_max)

        hsv_min = np.array([150,127,0])
        hsv_max = np.array([179,255,255])
        mask2 = cv2.inRange(hsv, hsv_min, hsv_max)

        return mask1 + mask2

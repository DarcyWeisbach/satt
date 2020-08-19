#!/usr/bin/env python
        # -*- coding: utf-8 -*-

class satt:
    def discretization(array1,array2,number):
        area = [0,0,0,0,0]
        for i in range(number):
            if 0<=array1[i][0]<120:
                area[0]+=array2[i][4]
            if 120<=array1[i][0]<240:
                area[1]+=array2[i][4]
            if 240<=array1[i][0]<=360:
                area[2]+=array2[i][4]
            if 360<array1[i][0]<=480:
                area[3]+=array2[i][4]
            if 480<array1[i][0]<=600:
                area[4]+=array2[i][4]
        return area

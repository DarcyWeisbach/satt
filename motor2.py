#!/usr/bin/env python
        # -*- coding: utf-8 -*-
import time
import wiringpi
motor1_pin = 5
motor2_pin = 6
motor3_pin = 13
motor4_pin = 19
def go(second):
    if second == 0:
        print("回転")
    else:
        print(str(second)+"秒回転")
    wiringpi.digitalWrite( motor1_pin, 1 )
    wiringpi.digitalWrite( motor2_pin, 0 )
    wiringpi.digitalWrite( motor3_pin, 1 )
    wiringpi.digitalWrite( motor4_pin, 0 )
    time.sleep(second)

def back(second):
    if second == 0:
        print("後転 ")
    else:
        print(str(second)+"秒逆回転")
        wiringpi.digitalWrite( motor1_pin, 0 )
        wiringpi.digitalWrite( motor2_pin, 1 )
        wiringpi.digitalWrite( motor3_pin, 0 )
        wiringpi.digitalWrite( motor4_pin, 1 )
        time.sleep(second)

def right(second):
    if second == 0:
        print("right回転")
    else:
        print(str(second)+"秒逆回転")
        wiringpi.digitalWrite( motor1_pin, 1 )"""modify"""
        wiringpi.digitalWrite( motor2_pin, 0 )
        wiringpi.digitalWrite( motor3_pin, 0 )
        wiringpi.digitalWrite( motor4_pin, 1 )
        time.sleep(second)
def left(second):
    if second == 0:
        print("left回転")
    else:
        print(str(second)+"秒逆回転")
        wiringpi.digitalWrite( motor1_pin, 0 )
        wiringpi.digitalWrite( motor2_pin, 1 )
        wiringpi.digitalWrite( motor3_pin, 1 )
        wiringpi.digitalWrite( motor4_pin, 0 )
        time.sleep(second)
def breake():
    print("ブレーキ！")
    wiringpi.digitalWrite( motor1_pin, 1 )
    wiringpi.digitalWrite( motor2_pin, 1 )
    wiringpi.digitalWrite( motor3_pin, 1 )
    wiringpi.digitalWrite( motor4_pin, 1 )
"""high-level function"""
def Motor(max_location_index,func0=go,func1=right,func2=left,func3=breake):
    wiringpi.wiringPiSetupGpio()
    wiringpi.pinMode( motor1_pin, 1 )
    wiringpi.pinMode( motor2_pin, 1 )
    wiringpi.pinMode( motor3_pin, 1 )
    wiringpi.pinMode( motor4_pin, 1 )

    if max_location_index == 0:
        return func2(1)
    if max_location_index == 1:
        return func2(0.5)
    if max_location_index == 2:
        return func0(3)
    if max_location_index == 3:
        return func1(0.5)
    if max_location_index == 4:
        return func1(1)

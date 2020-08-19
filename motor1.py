# GPIOを制御するライブラリ
#importwiringpi wiringpiをimportしてください
# タイマーのライブラリ
#importtime　timeをimportしてください
import time
import wiringpi
motor1_pin = 23 #16
motor2_pin = 24 #18

motor3_pin = 5 #29
motor4_pin = 6 #31
def Motor(max_location_index):
    # GPIO端子の設定
    #motor1_pin = 23 #16
    #motor2_pin = 24 #18
    #motor3_pin = 5 #29
    #motor4_pin = 6 #31

    # GPIO出力モードを1に設定する
    wiringpi.wiringPiSetupGpio()
    wiringpi.pinMode( motor1_pin, 1 )
    wiringpi.pinMode( motor2_pin, 1 )
    wiringpi.pinMode( motor3_pin, 1 )
    wiringpi.pinMode( motor4_pin, 1 )
    '''what's happened! it's strange.please check where motor3 and  motor4 is  '''
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
            wiringpi.digitalWrite( motor1_pin, 0 )
            wiringpi.digitalWrite( motor2_pin, 1 )
            wiringpi.digitalWrite( motor3_pin, 1 )
            wiringpi.digitalWrite( motor4_pin, 0 )
            time.sleep(second)
    def left(second):
        if second == 0:
            print("left回転")
        else:
            print(str(second)+"秒逆回転")
            wiringpi.digitalWrite( motor1_pin, 1 )
            wiringpi.digitalWrite( motor2_pin, 0 )
            wiringpi.digitalWrite( motor3_pin, 0 )
            wiringpi.digitalWrite( motor4_pin, 1 )
            time.sleep(second)
# 第2引数が0の場合は、ブレーキをしない
# 第1引数がbreakの場合は、ブレーキ
    def breake():
        print("ブレーキ！")
        wiringpi.digitalWrite( motor1_pin, 1 )
        wiringpi.digitalWrite( motor2_pin, 1 )
        wiringpi.digitalWrite( motor3_pin, 1 )
        wiringpi.digitalWrite( motor4_pin, 1 )
    # time is temporary,so we should modify this after
    if max_location_index == 0:
        return left(2)
    if max_location_index == 1:
        return left(1)
    if max_location_index == 2:
        return go(1)
    if max_location_index == 3:
        return right(1)
    if max_location_index == 4:
        return right(2)

from MS5607 import MS5607
import time
import csv

f=open("data_MS5607.csv","w")
i=0
all = 0
pre = 0

while True:


    sensor = MS5607()
    temperature = sensor.getDigitalTemperature()
    pressure = sensor.getDigitalPressure()
    converted = sensor.convertPressureTemperature(pressure,temperature)
    altitude = sensor.getMetricAltitude(converted,sensor.inHgToHectoPascal(29.95))

    converted = converted /100
    if i < 10:
        all = all + altitude
        if i == 9:
            average = all/10

    if i>=10:
        #b="\n"
        #f.write(str(altitude)+b)
        #print("height:%f"%altitude)
        altitude = altitude - average

        print(altitude)
        #print("                    difference:%lf"%(altitude-pre))
        #print("pressure:%.1f [hPa]"%converted)

        writer=csv.writer(f,lineterminator='\n')
        writer.writerow([altitude])


    time.sleep(0.3)
    i= i + 1
    pre = altitude

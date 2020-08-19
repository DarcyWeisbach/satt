from MS5607 import MS5607

sensor = MS5607()
temperature = sensor.getDigitalTemperature()
pressure = sensor.getDigitalPressure()
converted = sensor.convertPressureTemperature(pressure, temperature)
altitude = sensor.getMetricAltitude(converted, sensor.inHgToHectoPascal(29.95)) #set the altimeter setting appropriately

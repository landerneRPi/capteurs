from ds18b20 import DS18B20

sensor = DS18B20()
temperature_celsius = sensor.get_temperature()
print("température=",temperature_celsius)

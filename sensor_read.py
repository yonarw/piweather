
import subprocess
import time
import RPi.GPIO as GPIO
import bme280

def readTempI2C():
    try:
        res = subprocess.run(["cat","/sys/bus/w1/devices/28-0417822adbff/temperature"],stdout=subprocess.PIPE)
        tmpstr = res.stdout.decode('utf-8')
        tmp = float(tmpstr)
        return tmp/1000.0
    except:
        print("error while reading tmp!")
    return 0.0

def readBME280():
    try:
        temperature,pressure,humidity = bme280.readBME280All()
        return (temperature,pressure,humidity)
    except:
        print("error reading bme280")
        return (0,0,0)

def getWeatherInfo():
    temperature,pressure,humidity = readBME280()
    return {"temperature":readTempI2C(),"temperature2":temperature,
            "humidity":humidity,"pressure":pressure}

if __name__ == "__main__":
    while True:        
        for k,v in getWeatherInfo():
            print(k," = ",v)
        print("-------------------")
        time.sleep(1)

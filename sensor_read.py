
import subprocess
import time
import RPi.GPIO as GPIO
#import dht11
import bme280

def readTemp():
    try:
        res = subprocess.run(["cat","/sys/bus/w1/devices/28-0417822adbff/temperature"],stdout=subprocess.PIPE)
        tmpstr = res.stdout.decode('utf-8')
        tmp = float(tmpstr)
        return tmp/1000.0
    except:
        print("error while reading tmp!")
    return 0.0

# def readHum():
#     instance = dht11.DHT11(pin = 17)
#     res = instance.read()
#     while not res.is_valid():
#         res = instance.read()
#     tmp = res.temperature
#     hum = res.humidity
#     return (tmp,hum)

def readBME280():
    try:
        temperature,pressure,humidity = bme280.readBME280All()
        return (temperature,pressure,humidity)
    except:
        print("error reading bme280")
        return (0,0,0)

prev_hum = (0.0,0.0)

def setupGPIO():
     # initialize GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()

def getWeatherInfo():
    temperature,pressure,humidity = readBME280()
    return {"temperature":readTemp(),"temperature2":temperature,
            "humidity":humidity,"pressure":pressure}

if __name__ == "__main__":
    setupGPIO()
    prev = (0.0,0.0)
    while True:
        d = getWeatherInfo()
        for a in d:
            print(a,"=",d[a])
        print("-------------------")
        time.sleep(1)

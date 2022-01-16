# piweather -  simple rest-api server and sensor updater for raspberry pi

Note sensors are hard coded. Remember to enable I2C and change sensor(s) in [sensor_read.py](sensor_read.py)

To auto-start the service one option is the file `/etc/rc.local` 

```shell
...

cd <path-to-repository-on-raspberry-pi>
python3 service.py &

...

```


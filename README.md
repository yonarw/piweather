# piweather -  simple rest-api server and sensor updater for raspberry pi

Note sensors are hard coded. Remember to enable I2C and change sensor(s) in [sensor_read.py](sensor_read.py)

To auto-start the service one option is the file `/etc/rc.local` 

```shell
...

cd <path-to-repository-on-raspberry-pi>
python3 service.py &

...

```

To readout the sensors in Home Assistant add this to the `sensor` section in your `configuration.yaml`
```yaml
sensor:
  - platform: rest
    name: raspi_sensors
    resource: http://<ip-of-raspberry-pi>:5000/sensor/state
    value_template: 'OK'
    scan_interval: 60
    json_attributes:
      - temperature
      - temperature2
      - humidity
      - pressure
  - platform: template
      sensors:
        outside_temperature:
          value_template: "{{ state_attr('sensor.raspi_sensors','temperature') | round(2) }}"
          device_class: temperature
          unit_of_measurement: "°C"
        outside_temperature2:
          value_template: "{{ state_attr('sensor.raspi_sensors','temperature2') | round(2) }}"
          device_class: temperature
          unit_of_measurement: "°C"
        outside_humidity:
          value_template: "{{ state_attr('sensor.raspi_sensors','humidity') | round(2) }}"
          device_class: humidity
          unit_of_measurement: "%"
        outside_pressure:
          value_template: "{{ state_attr('sensor.raspi_sensors','pressure') | round(2) }}"
          device_class: pressure
          unit_of_measurement: "hPa"
```

import json
import sensor_read
import threading
import time

from flask import Flask, request

sensor_read.setupGPIO()
curr_values = sensor_read.getWeatherInfo()

def updateWinfo():
    global curr_values
    while True:
        curr_values = sensor_read.getWeatherInfo()
        time.sleep(10*1)

def run_rest():
    app = Flask(__name__)

    @app.route('/sensor/state', methods=['GET'])
    def get_state():
        return json.dumps(curr_values)+"\n"
    print("Starting flask app!")
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    print("starting service!!!")
    t = threading.Thread(target = updateWinfo)
    t.start()
    run_rest()
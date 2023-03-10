import neopixel
import digitalio
import ssl
import wifi
import secrets
import settings
import functions
import socketpool
import adafruit_requests
import colors
import math

class HelperFunctions:

    @staticmethod
    def calc_voltage(val):
        #physical circuit goes through a voltage divider
        #so we double the reading to calc actual voltage
        return ((val * 3.3) / 65536) * 2

    @staticmethod
    def get_gyro_motion(gyro):
        #print("Gyro X:%.2f, Y: %.2f, Z: %.2f rads/s" % (gyro))
        x = abs(gyro[0])
        y = abs(gyro[1])
        z = abs(gyro[2])
        return max([x,y,z])

    def get_temperature(thermistor):
        r = 10000 / (65535/thermistor.value - 1)
        steinhart = math.log(r / 10000.0) / 3950.0
        steinhart += 1.0 / (25.0 + 273.15)
        steinhart = (1.0 / steinhart) - 273.15
        return steinhart


class NetFunctions:

    def __init__(self):
        self.pool = socketpool.SocketPool(wifi.radio)
        self.requests = adafruit_requests.Session(self.pool, ssl.create_default_context())
        self.errors = []

    def flush_errors(self):
        err = self.errors.copy()
        self.errors = []
        return err

    def connect_wifi(self, led):
        led.fill(colors.led_yellow)
        ssid = secrets.ssid
        password = secrets.password
        wifi.radio.enabled = True
        wifi.radio.hostname = 'CompostBuddy-ESP32'
        try:
            wifi.radio.connect(ssid, password)
            led.fill(colors.led_blue)
            return True
        except Exception as e:
            print(str(e))
            self.errors.append(str(e))
            return False

    def disconnect_wifi(self, led):
        wifi.radio.enabled = False
        led.fill(colors.led_off)
        return True

    def post_json(self, endpoint, obj):
        if wifi.radio.enabled:
            try:
                response = self.requests.post(secrets.apiURI + endpoint, json=obj)
                return response.text
            except Exception as e:
                print(str(e))
                self.errors.append(str(e))
                return ''
        else:
            return ''

    def http_get_text(self, uri):
        if wifi.radio.enabled:
            try:
                response = self.requests.get(secrets.apiURI + uri)
                return response.text
            except Exception as e:
                print(str(e))
                self.errors.append(str(e))
                return ''
        else:
            return ''

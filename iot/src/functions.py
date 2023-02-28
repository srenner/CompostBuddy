import time
import board
import neopixel
import digitalio
import ssl
import wifi
import secrets
import settings
import functions
import adafruit_httpserver
import socketpool
import adafruit_requests
import adafruit_icm20x
import colors

class HelperFunctions:

    @staticmethod
    def calc_voltage(val):
        return (val * 3.3) / 65536

    @staticmethod
    def get_gyro_motion(gyro):
        #print("Gyro X:%.2f, Y: %.2f, Z: %.2f rads/s" % (gyro))
        x = abs(gyro[0])
        y = abs(gyro[1])
        z = abs(gyro[2])
        return max([x,y,z])


class NetFunctions:

    def __init__(self):
        self.pool = socketpool.SocketPool(wifi.radio)
        self.requests = adafruit_requests.Session(self.pool, ssl.create_default_context())

    def connect_wifi(self, led):
        led.fill(colors.led_yellow)
        ssid = secrets.ssid
        password = secrets.password
        wifi.radio.enabled = True
        wifi.radio.hostname = 'CompostBuddy-ESP32'
        wifi.radio.connect(ssid, password)
        led.fill(colors.led_blue)
        return True

    def disconnect_wifi(self, led):
        wifi.radio.enabled = False
        led.fill(colors.led_off)
        return True

    def post_debug(self, obj):
        if wifi.radio.enabled:
            response = self.requests.post(secrets.apiURI + "debug", json=obj)
            return response.text
        else:
            return ''

    def http_get_text(self, uri):
        if wifi.radio.enabled:
            response = self.requests.get(secrets.apiURI + uri)
            return response.text
        else:
            return ''

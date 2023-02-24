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

class Functions:
    @staticmethod
    def connect_wifi(led):
        led.fill(colors.led_yellow)
        ssid = secrets.ssid
        password = secrets.password
        wifi.radio.enabled = True
        wifi.radio.hostname = 'CompostBuddy-ESP32'
        wifi.radio.connect(ssid, password)
        if settings.DEBUG:
            print('\n' + wifi.radio.hostname + " IPv4 " + str(wifi.radio.ipv4_address))
        led.fill(colors.led_blue)
        return True

    @staticmethod
    def disconnect_wifi(led):
        wifi.radio.enabled = False
        if settings.DEBUG:
            print('\n' + "Disconnected from WiFi")
        led.fill(colors.led_off)
        return True

    @staticmethod
    def get_datetime():
        if wifi.radio.enabled:
            pool = socketpool.SocketPool(wifi.radio)
            requests = adafruit_requests.Session(pool, ssl.create_default_context())
            response = requests.get(secrets.apiURI + "datetime")
            return response.text
        else:
            return ''

    @staticmethod
    def get_api_version():
        if wifi.radio.enabled:
            pool = socketpool.SocketPool(wifi.radio)
            requests = adafruit_requests.Session(pool, ssl.create_default_context())
            response = requests.get(secrets.apiURI + "version")
            return response.text
        else:
            return ''

    @staticmethod
    def get_gyro_motion(gyro):
        #print("Gyro X:%.2f, Y: %.2f, Z: %.2f rads/s" % (gyro))
        x = abs(gyro[0])
        y = abs(gyro[1])
        z = abs(gyro[2])
        return max([x,y,z])

import time
import board
import neopixel
import digitalio
import ssl
import wifi
import secrets
import functions
import adafruit_httpserver
import socketpool
import adafruit_requests
import adafruit_icm20x

class Functions:
    @staticmethod
    def connect_wifi():
        ssid = secrets.ssid
        password = secrets.password
        wifi.radio.enabled = True
        wifi.radio.hostname = 'CompostBuddy-ESP32'
        wifi.radio.connect(ssid, password)
        print('\n' + wifi.radio.hostname + " IPv4 " + str(wifi.radio.ipv4_address))

        pool = socketpool.SocketPool(wifi.radio)
        requests = adafruit_requests.Session(pool, ssl.create_default_context())
        response = requests.get(secrets.apiURI + "version")
        print(f"Using CompostBuddy API {response.text}")
        return True

    @staticmethod
    def disconnect_wifi():
        wifi.radio.enabled = False
        print('\n' + "Disconnected from WiFi")
        return True

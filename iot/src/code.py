# SPDX-FileCopyrightText: 2023
#
# SPDX-License-Identifier: MIT

import time
import board
import neopixel
import digitalio
import ssl
import wifi
import secrets
import adafruit_httpserver
import socketpool
import adafruit_requests

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixels.fill(red)

ssid = secrets.ssid
password = secrets.password
wifi.radio.hostname = 'CompostBuddy-ESP32'
print("Connecting to", ssid)
wifi.radio.connect(ssid, password)
print("Connected to", ssid)
#print(f"Listening on http://{wifi.radio.ipv4_address}")
print(wifi.radio.hostname + " IPv4 " + str(wifi.radio.ipv4_address))

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())
response = requests.get(secrets.apiURI + "version")
print(f"Using CompostBuddy API {response.text}")

x = 0
while True:
    pixels.fill(white)
    time.sleep(0.5)
    pixels.fill(red)
    time.sleep(0.5)
    pixels.fill(green)
    time.sleep(0.5)
    x = x + 1
    print(x)

print("Goodbye")

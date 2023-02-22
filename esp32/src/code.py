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

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixels.fill(red)



x = 0

ssid = secrets.ssid
password = secrets.password
wifi.radio.hostname = 'CompostBuddy-ESP32'
print("Connecting to", ssid)
wifi.radio.connect(ssid, password)
print("Connected to", ssid)
print(f"Listening on http://{wifi.radio.ipv4_address}")

#requests = adafruit_requests.Session(pool, ssl.create_default_context())


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

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
from functions import Functions
import adafruit_httpserver
import socketpool
import adafruit_requests
import adafruit_icm20x

led_white = (50, 50, 50)
led_red = (50, 0, 0)
led_green = (0, 1, 0)
led_off = (0, 0, 0)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

if Functions.connect_wifi():
    pixels.fill(led_green)

i2c = board.STEMMA_I2C()
icm = adafruit_icm20x.ICM20948(i2c)

if Functions.disconnect_wifi():
    pixels.fill(led_off)

while True:
    #print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (icm.acceleration))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f rads/s" % (icm.gyro))
    #print("Magnetometer X:%.2f, Y: %.2f, Z: %.2f uT" % (icm.magnetic))
    #print("")
    time.sleep(1)

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

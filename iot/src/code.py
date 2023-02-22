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
#import supervisor

# SETUP ##########################################################################

led_white = (50, 50, 50)
led_red = (50, 0, 0)
led_green = (0, 1, 0)
led_off = (0, 0, 0)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

pixels.fill(led_red)

i2c = board.STEMMA_I2C()
icm = adafruit_icm20x.ICM20948(i2c)

last_gyro = 0.0
current_gyro = 0.0
is_turning = False
last_turn = 0.0

bin1_temp = 10.0
bin2_temp = 10.0

pixels.fill(led_off)

# LOGIC ##########################################################################

# Functions.connect_wifi(pixels, led_green)
# time.sleep(1)
# Functions.disconnect_wifi(pixels, led_off)

last_gyro = 0.0
current_gyro = 0.0

while True:
    #print("Gyro X:%.2f, Y: %.2f, Z: %.2f rads/s" % (icm.gyro))
    #print(time.monotonic())

    current_gyro = Functions.get_gyro_motion(icm.gyro)

    if current_gyro > 1.0 and last_gyro > 1.0:
        print("Turning")
    else:
        print("")

    last_gyro = current_gyro
    time.sleep(1)

print("Bye!")

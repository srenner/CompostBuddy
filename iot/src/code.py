# SPDX-FileCopyrightText: 2023
#
# SPDX-License-Identifier: MIT

import collections
from collections import deque
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
import array
import colors
#import supervisor

# SETUP ##########################################################################


pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

pixels.fill(colors.led_red)

i2c = board.STEMMA_I2C()
icm = adafruit_icm20x.ICM20948(i2c)

is_turning = False
was_turning = False
last_turn = 'unknown'

bin1_temp = 10.0
bin2_temp = 10.0

pixels.fill(colors.led_off)

# LOGIC ##########################################################################

# Functions.connect_wifi(pixels, led_green)
# Functions.disconnect_wifi(pixels, led_off)

turn_buffer = array.array('f', [0,0,0,0,0,0,0,0,0,0])
tb_idx = 0

while True:
    current_gyro = Functions.get_gyro_motion(icm.gyro)

    if tb_idx > 9:
        tb_idx = 0
    turn_buffer[tb_idx] = current_gyro
    #print(turn_buffer)
    #print(sum(turn_buffer))
    is_turning = sum(turn_buffer) > 10
    #print(is_turning)
    tb_idx += 1


    if is_turning == False and was_turning == True:
        Functions.connect_wifi(pixels)

        last_turn = Functions.get_datetime()

        Functions.disconnect_wifi(pixels)



    was_turning = is_turning

    if is_turning:
        print("turning now")
    else:
        print(f"last turn", last_turn)

    time.sleep(1)

print("Bye!")

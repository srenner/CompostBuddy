# SPDX-FileCopyrightText: 2023
#
# SPDX-License-Identifier: MIT

import time
import board
import neopixel
import digitalio
from functions import Functions
import adafruit_icm20x
import array
import colors
import secrets
import settings
import json

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

turn_buffer = array.array('f', [0,0,0,0,0,0,0,0,0,0])
tb_idx = 0

current_time = time.time()
next_json = current_time + settings.json_interval
next_post = current_time + settings.post_interval

pixels.fill(colors.led_off)

# LOGIC ##########################################################################

#print(time.time())

while True:


    current_gyro = Functions.get_gyro_motion(icm.gyro)

    if tb_idx > 9:
        tb_idx = 0
    turn_buffer[tb_idx] = current_gyro
    is_turning = sum(turn_buffer) > 10
    tb_idx += 1

    if is_turning == False and was_turning == True:
        Functions.connect_wifi(pixels)
        last_turn = Functions.get_datetime()
        Functions.disconnect_wifi(pixels)

    was_turning = is_turning

    if settings.DEBUG:
        if is_turning:
            print("turning now")
        else:
            print(f"last turn", last_turn)

    current_time = time.time()
    if current_time >= next_json:
        print("create json object now")
        next_json = current_time + settings.json_interval
    if current_time >= next_post:
        print("post data now")
        next_post = current_time + settings.post_interval

    time.sleep(1)

print("Bye!")

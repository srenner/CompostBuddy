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
import adafruit_thermistor

# SETUP ##########################################################################

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)

pixels.fill(colors.led_red)

i2c = board.STEMMA_I2C()
icm = adafruit_icm20x.ICM20948(i2c)

therm1 = adafruit_thermistor.Thermistor(board.A0, 10000, 10000, 25, 3950)
therm2 = adafruit_thermistor.Thermistor(board.A1, 10000, 10000, 25, 3950)
bin1_temp = 0.0
bin1_buf = [0.0,0.0,0.0]
bin2_temp = 0.0
bin2_buf = [0.0,0.0,0.0]

is_turning = False
was_turning = False
last_turn = 'unknown'

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

        bin1_buf[0] = therm1.temperature
        bin2_buf[0] = therm2.temperature
        time.sleep(.1)
        bin1_buf[1] = therm1.temperature
        bin2_buf[1] = therm2.temperature
        time.sleep(.1)
        bin1_buf[2] = therm1.temperature
        bin2_buf[2] = therm2.temperature

        bin1_temp = sum(bin1_buf) / len(bin1_buf)
        bin2_temp = sum(bin2_buf) / len(bin2_buf)

        print(f"bin1: {bin1_buf}")
        print(f"bin1: {bin1_temp}")
        print(f"bin2: {bin2_buf}")
        print(f"bin2: {bin2_temp}")

        next_json = current_time + settings.json_interval
    if current_time >= next_post:
        print("post data now")
        next_post = current_time + settings.post_interval

    time.sleep(1)

print("Bye!")

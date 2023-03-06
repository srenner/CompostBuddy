# SPDX-FileCopyrightText: 2023
#
# SPDX-License-Identifier: MIT

import time
import board
import neopixel
import digitalio
import analogio
from functions import HelperFunctions, NetFunctions
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

netFuncs = NetFunctions()

i2c = board.STEMMA_I2C()
icm = adafruit_icm20x.ICM20948(i2c)

therm1 = adafruit_thermistor.Thermistor(board.A0, 10000, 10000, 25, 3950)
therm2 = adafruit_thermistor.Thermistor(board.A1, 10000, 10000, 25, 3950)
bin1_temp = therm1.temperature
bin1_buf = [0.0,0.0,0.0]
bin2_temp = therm2.temperature
bin2_buf = [0.0,0.0,0.0]

is_turning = False
was_turning = False
last_turn = 'unknown'

turn_buffer = array.array('f', [0,0,0,0,0,0,0,0,0,0])
tb_idx = 0

# pgood indicates if the battery charger has a valid power source connected
pgood = digitalio.DigitalInOut(board.D37) #SPI MI
pgood.direction = digitalio.Direction.INPUT

# chg indicates if the battery charger is actively charging the battery
chg = digitalio.DigitalInOut(board.D35) # SPI MO
chg.direction = digitalio.Direction.INPUT

# voltage of the 3.7/4.2v battery that powers the board
voltageInput = analogio.AnalogIn(board.A2)

current_time = time.time()
next_json = current_time + settings.json_interval
next_post = current_time + settings.post_interval

if settings.DEBUG:
    print("\n")
    print(f"temp:", bin1_temp, bin2_temp)
    print(f"volts:", HelperFunctions.calc_voltage(voltageInput.value))
    print("pgood:", not pgood.value)
    print("chg:", not chg.value)

pixels.fill(colors.led_off)

# LOGIC ##########################################################################

while True:
    current_gyro = HelperFunctions.get_gyro_motion(icm.gyro)

    #add item to gyroscope buffer to determine if the barrel is currently turning
    if tb_idx > 9:
        tb_idx = 0
    turn_buffer[tb_idx] = current_gyro
    is_turning = sum(turn_buffer) > 10
    tb_idx += 1
    if is_turning == False and was_turning == True:
        #turning is finished, set last_turn to be used in the next json post
        netFuncs.connect_wifi(pixels)
        last_turn = netFuncs.http_get_text("datetime")
        netFuncs.disconnect_wifi(pixels)
    was_turning = is_turning

    current_time = time.time()
    if current_time >= next_json:
        print("create json object now")

        chargerAvailable = not pgood.value
        charging = not chg.value

        if settings.DEBUG:
            print("pgood:", str(chargerAvailable))
            print("chg:", str(charging))


        if settings.use_temperature_buffers:
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
        else:
            bin1_temp = therm1.temperature
            bin2_temp = therm2.temperature

        print(f"bin1: {bin1_temp}")
        print(f"bin2: {bin2_temp}")

        volts = HelperFunctions.calc_voltage(voltageInput.value)

        #print(f"volts: {volts}")

        netFuncs.connect_wifi(pixels)
        reqBody = json.loads("{\"volts\": " + str(volts) + "}")
        netFuncs.post_debug(reqBody)
        print(netFuncs.http_get_text("datetime"))
        netFuncs.disconnect_wifi(pixels)

        next_json = current_time + settings.json_interval

    if current_time >= next_post:
        print("post data now")

        errors = netFuncs.flush_errors()
        print(errors)

        next_post = current_time + settings.post_interval

    time.sleep(settings.loop_interval)

print("Bye!")

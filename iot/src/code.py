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
import settings
import json
import alarm

# SETUP ##########################################################################

led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.fill(colors.led_red)

netFuncs = NetFunctions()

i2c = board.STEMMA_I2C()
icm = adafruit_icm20x.ICM20948(i2c)

therm1 = analogio.AnalogIn(board.A1)
therm2 = analogio.AnalogIn(board.A0)

bin1_temp = HelperFunctions.get_temperature(therm1)
bin1_buf = [0.0,0.0,0.0]
bin2_temp = HelperFunctions.get_temperature(therm2)
bin2_buf = [0.0,0.0,0.0]

is_turning = False
was_turning = False
last_turn = ''

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
volts = HelperFunctions.calc_voltage(voltageInput.value)
print("startup voltage: " + str(volts))

current_time = time.time()
next_json = current_time + settings.json_interval
next_post = current_time + settings.post_interval

if settings.DEBUG:
    print("\n")
    print(f"temp:", bin1_temp, bin2_temp)
    print(f"volts:", HelperFunctions.calc_voltage(voltageInput.value))
    print("pgood:", not pgood.value)
    print("chg:", not chg.value)

post_body = []

led.fill(colors.led_off)

# LOGIC ##########################################################################

while True:
    current_gyro = HelperFunctions.get_gyro_motion(icm.gyro)

    #add item to gyroscope buffer to determine if the barrel is currently turning
    if tb_idx > 9:
        tb_idx = 0
    turn_buffer[tb_idx] = current_gyro
    is_turning = sum(turn_buffer) > 1
    tb_idx += 1
    if is_turning == False and was_turning == True:
        #turning is finished, set last_turn to be used in the next json post
        netFuncs.connect_wifi(led)
        last_turn = netFuncs.http_get_text("datetime")
        netFuncs.disconnect_wifi(led)
    was_turning = is_turning

    current_time = time.time()
    if current_time >= next_json:
        print("Building JSON Object")

        chargerAvailable = not pgood.value
        charging = not chg.value

        if settings.DEBUG:
            print("pgood:", str(chargerAvailable))
            print("chg:", str(charging))

        if settings.use_temperature_buffers:
            bin1_buf[0] = HelperFunctions.get_temperature(therm1)
            bin2_buf[0] = HelperFunctions.get_temperature(therm2)
            time.sleep(.1)
            bin1_buf[1] = HelperFunctions.get_temperature(therm1)
            bin2_buf[1] = HelperFunctions.get_temperature(therm2)
            time.sleep(.1)
            bin1_buf[2] = HelperFunctions.get_temperature(therm1)
            bin2_buf[2] = HelperFunctions.get_temperature(therm2)
            bin1_temp = sum(bin1_buf) / len(bin1_buf)
            bin2_temp = sum(bin2_buf) / len(bin2_buf)
        else:
            bin1_temp = HelperFunctions.get_temperature(therm1)
            bin2_temp = HelperFunctions.get_temperature(therm2)

        if settings.DEBUG:
            print(f"bin1: {HelperFunctions.get_temperature(therm1)}")
            print(f"bin2: {HelperFunctions.get_temperature(therm2)}")

        volts = HelperFunctions.calc_voltage(voltageInput.value)

        datapoint = {
            "timeref": time.time(),
            "temp1": bin1_temp,
            "temp2": bin2_temp,
            "vbat": volts,
            "last_turn": last_turn,
            "power": chargerAvailable,
            "charging": charging,
            "errors": netFuncs.flush_errors()
        }

        post_body.append(datapoint)

        next_json = current_time + (settings.json_interval * settings.low_power_multiplier)

    if current_time >= next_post:
        print("POSTing Data")

        netFuncs.connect_wifi(led)
        netFuncs.post_json("events", post_body)
        netFuncs.disconnect_wifi(led)

        post_body = []

        if volts < 3.6:
            low_power_multiplier = 2
            if volts < 3.4:
                time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 3600)
                alarm.exit_and_deep_sleep_until_alarms(time_alarm)
        else:
            low_power_multiplier = 1

        next_post = current_time + (settings.post_interval * settings.low_power_multiplier)

    time.sleep(settings.loop_interval * settings.low_power_multiplier)

print("Bye!")

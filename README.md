# CompostBuddy

![CompostBuddy IoT Device](doc/CompostBuddy.jpg)

IoT project to assist with home composting. Uses a ESP32 microcontroller and a minimal self-hosted companion app.

## Description

This is a WiFi connected IoT project that monitors a home compost tumbler. The system monitors compost temperature and tumbling frequency. The system knows when the compost has been turned based on gyroscope data. The temperature probes indicate if the compost is actively decomposing.

## Tech in Use
- CircuitPython
- Express
- MongoDB
- Vue 3
- Bootstrap 5

## Hardware
- ESP32 based microcontroller
- Gyroscope
- Thermistor probes
- Solar power system (solar cells, lipo battery, controller board, etc.)
- Local machine as web host

## Possible future enhancements
- Push notifications and data visibility powered by Home Assistant

## Useful links
- [Compost info from Cornell University](https://compost.css.cornell.edu/microorg.html)
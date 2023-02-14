# CompostBuddy

IoT project to assist with home composting. Uses a ESP32 microcontroller, a minimal self-hosted companion app, and automation routines powered by Home Assistant.

## Description

This is a WiFi connected IoT project that monitors a home compost tumbler. The system monitors compost temperature and sends reminders (via Home Assistant) when the compost needs to be "turned." The system knows when the compost has been turned based on accelerometer data.

With the help of modern technology, we will grow the best tomatoes the world has ever tasted.

## Hardware
- ESP32 based microcontroller
- Accelerometer (tbd)
- Thermocouple probes and related hardware (tbd)
- Solar power system (solar cells, lipo battery, controller board, etc.)
- Local installation of Home Assistant 
- Local machine as web host
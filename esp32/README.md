# CompostBuddy IoT

## Bill of Materials
| Item                                                   | Link                                        |
| ---                                                    | ---                                         |
| Adafruit QT Py ESP32-S3 WiFi Dev Board                 | https://www.adafruit.com/product/5426       |
| 10K Precision Epoxy Thermistor (x2)                    | https://www.adafruit.com/product/372        |
| TDK InvenSense ICM-20948 9-DoF IMU                     | https://www.adafruit.com/product/4554       |
| Lithium Ion Polymer Battery - 3.7v 2500mAh             | https://www.adafruit.com/product/328        |
| Universal USB / DC / Solar Lithium Ion/Polymer charger | https://www.adafruit.com/product/4755       |
| 6V 2W Solar Panel                                      | https://www.adafruit.com/product/5366       |
| 3.5mm / 1.1mm to 5.5mm / 2.1mm DC Jack Adapter         | https://www.adafruit.com/product/4287       |
| Weatherproof project box                               |                                             |
| Mounting hardware                                      |                                             |


## Example data to push to the server
~~~
{
    "timestamp": { "$date": "2023-02-15T17:09:43.942Z" },
    "info": [],
    "warnings": [
        "low battery"
    ],
    "errors": [],
    "uptime": 777600,
    "lastTurn": 604800,
    "batt": 28,
    "battStatus": "discharging",
    "bin1": {
        "temp": 54.4,
        "status": "active"
    },
    "bin2": {
        "temp": 20.1,
        "status": "idle"
    }
}
~~~

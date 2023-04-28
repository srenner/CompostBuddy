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
[
	{
		"timestamp": "2023-04-28T21:42:28.208Z",
		"batchDate": "2023-04-28T21:42:28.208Z",
		"_id": "644c3dc48ae2171ea0a00647",
		"temp2": 32.1522,
		"temp1": 27.7572,
		"timeref": 946837540,
		"vbat": 3.52589,
		"charging": true,
		"power": true,
		"last_turn": "",
		"errors": [
			"Unknown failure 6",
			"Sending request failed"
		]
	}
]
~~~

## TODO
* Use tilt detection interrupt instead of gyroscope if possible
* Implement custom instructions from API calls


## Useful links
* [Gyroscopes and accelerometers](https://www.analog.com/en/technical-articles/accelerometer-and-gyroscopes-sensors-operation-sensing-and-applications.html)
* [LSM6DS33 Datasheet](https://web.archive.org/web/20201103021503/https://www.st.com/resource/en/datasheet/lsm6ds33.pdf)

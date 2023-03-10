# CompostBuddy API

| URI                 | Method | Parameters                       | Purpose                               | Example output              |
| ---                 | ---    | ---                              | ---                                   | ---                         |
| /api/datetime       | GET    | [none]                           | Get timestamp for devices without RTC | 2023-03-10T14:46:44.154Z    |
| /api/version        | GET    | [none]                           | (future use)                          | 1.0.0-alpha                 |
| /api/event/latest   | GET    | [none]                           | Gets current status                   | { "timestamp": "2023-03-10T14:46:19.273Z", <br>"power": false, <br>"temp1": 5.71851, <br>"vbat": 3.71985, <br>"charging": true, <br>"timeref": 947354695, <br>"last_turn": "2023-03-10T03:48:49.766Z", <br>"errors": [], <br>"\_id": "640b42bb1909e25cc8febfcf", <br>"temp2": 5.63025 } |
| /api/events         | GET    | ?start=2023-03-08&end=2023-03-18 | Gets collection of events             | (array of objects as above) |
| /api/compost        | POST   | event array in body              | Posts data to MongoDB                 | 200 OK                      |

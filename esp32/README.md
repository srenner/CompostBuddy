# Proposed Data Structures

## Heartbeat

~~~
{  
    "info": ["low power mode", "info2", "info3"],
    "warnings:" ["low battery", "warning2", "warning3"],
    "errors": ["unexpected restart", "error2", "error3"],
    "uptime": 777600,
    "lastTurn": 604800,
    "batt": 28,
    "battStatus": "discharging"
    "bin1": {
        "temp": 54.4,
        "status": "thermophilic"
    },
    "bin2": {
        "temp": 20.1,
        "status": "mesophilic"
    }
}
~~~
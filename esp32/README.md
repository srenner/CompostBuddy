# Proposed Data Structures

## Heartbeat

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
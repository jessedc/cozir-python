from datetime import datetime, timezone
from copy import deepcopy

co2_header = 'z'
co2f_header = 'Z'
tmp_header = 'T'
humid_header = 'H'


# https://www.influxdata.com/blog/getting-started-python-influxdb/
# {
#     "measurement": "brushEvents",
#     "tags": {
#         "user": "Carol",
#         "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
#     },
#     "time": "2018-03-28T8:01:00Z",
#     "fields": {
#         "duration": 127
#     }
# }

# Converts a line read from the wire into an array of influx DB points that can be serialised
def points_from_line(line: str):
    timestamp = datetime.now(timezone.utc).astimezone().isoformat()

    measure_base = {
        "measurement": "co2",
        "tags": {
            "sensor": "cozir",
            "location": "bedroom2"
        },
        "time": timestamp,
        "fields": {}
    }

    measurements = []

    #  H 00486 T 01179 Z 01387 z 01377\r\n
    splits = line.split()
    i = 0
    while i < (len(splits) - 1):
        key = splits[i]
        val = int(splits[i + 1].lstrip('0'))
        i += 2
        measurement = deepcopy(measure_base)

        if key == tmp_header:
            val = float(val - 1000) / 10.0
            measurement["measurement"] = "temperature"
            measurement["fields"] = {"temp": val}
        elif key == humid_header:
            val = float(val) / 10.0
            measurement["measurement"] = "humidity"
            measurement["fields"] = {"humidity": val}
        elif key == co2f_header:
            measurement["fields"] = {"co2": val}
        else:
            # ignore other fields for now
            continue

        measurements.append(measurement)

    return measurements

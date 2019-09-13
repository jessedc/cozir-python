from datetime import datetime, timezone


co2_header = 'Z'
co2f_header = 'z'
tmp_header = 'T'
humid_header = 'H'


# Converts a line read from the wire into an array of influx DB points that can be serialised
def points_from_line(line: str):
    timestamp = datetime.now(timezone.utc).astimezone().isoformat()

    #  H 00486 T 01179 Z 01387 z 01377\r\n
    splits = line.split()
    params = [('ts', timestamp)]
    i = 0
    while i < (len(splits) - 1):
        key = splits[i]
        val = int(splits[i + 1].lstrip('0'))

        if key == tmp_header:
            val = float(val - 1000) / 10.0
        elif key == humid_header:
            val = float(val) / 10.0

        params.append((key, val))
        i += 2

    return params

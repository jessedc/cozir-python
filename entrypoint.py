#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cozir_python.linereader import LineReader
from cozir_python.influx import points_from_line
from influxdb import InfluxDBClient

# FIXME: Remove this from the global scope here
client = InfluxDBClient(host='pi.hole', port=8086)


def on_read_line_callback(line):
    if len(line.split()) % 2 != 0:
        print('Invalid line')
        return

    points = points_from_line(line)
    client.write_points(points, database='airquality')

    print(points)


if __name__ == "__main__":

    # On newer firmware/raspbian /dev/ttyAMA0 is sym linked to /dev/serial0
    reader = LineReader('/dev/serial0')
    reader.read_line_callback(on_read_line_callback)

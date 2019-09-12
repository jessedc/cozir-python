#!/usr/bin/env python3

from cozir import Cozir


def on_read_line_callback(line):
    print(line)


# On newer firmware/raspbian /dev/ttyAMA0 is sym linked to /dev/serial0
cozir = Cozir('/dev/serial0')
cozir.read_line_callback(on_read_line_callback)

from serial import Serial


class Cozir:

    def __init__(self, port, newline='\r\n'):
        self.port = port
        self.ser = Serial(port, 9600, timeout=1)
        self.line_end_header = newline
        self.co2_header = 'Z'
        self.co2f_header = 'z'
        self.tmp_header = 'T'
        self.humid_header = 'H'
        self.value = ''

    def input(self, byte):
        self.value += byte
        # check for \r\n at the end of our accumulated value
        if self.value[-2:] != self.line_end_header:
            return None

        #  H 00486 T 01179 Z 01387 z 01377\r\n
        line = self.value[:-2]
        self.value = ''

        splits = line.split()
        params = []
        i = 0
        while i < (len(splits) - 1):
            key = splits[i]
            val = int(splits[i + 1].lstrip('0'))

            if key == self.tmp_header:
                val = float(val - 1000) / 10.0
            elif key == self.humid_header:
                val = float(val) / 10.0

            params.append((key, val))
            i += 2

        return params

    def read_line_callback(self, callback):
        while True:
            byte = self.ser.read(1)
            if byte:
                line = self.input(byte)
                if line is not None:
                    callback(line)
            else:
                pass

from serial import Serial as SysSerial


class LineReader:

    def __init__(self, port, baudrate=9600, newline='\r\n'):
        self.ser = SysSerial(port, timeout=1, baudrate=baudrate)
        self.line_end_header = newline
        self.line_end_header_length = len(newline) * -1

        self.value = ''

    def input(self, byte):
        self.value += byte.decode('utf-8')

        if self.value[self.line_end_header_length:] != self.line_end_header:
            return None

        line = self.value[:self.line_end_header_length]
        self.value = ''

        return line

    def read_line_callback(self, callback):
        while True:
            byte = self.ser.read()
            if byte:
                line = self.input(byte)
                if line is not None:
                    callback(line)
            else:
                pass

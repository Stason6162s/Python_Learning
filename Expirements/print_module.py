class ZPLPrinter:
    import os
    import socket
    from serial import Serial, SerialException

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def com_print(self, data):
        serial_port = 'COM1' if os.name == 'nt' else "/dev/ttyS0"
        com_port = Serial(port=serial_port, baudrate=9600, dsrdtr=1, timeout=None)
        try:
            data_bytes = bytes('^XA^CI15^FO^A0N,50^FD{0}^FS^XZ'.format(data), 'UTF-8')
            com_port.write(data_bytes)
            print("\t Sent %s to print" % data)
        except self.SerialException:
            print('Error in com_print')

    def net_print(self, data):
        try:
            self_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self_socket.connect(('172.26.193.20', 9100))
            data = "^XA^CI15^FO^A0N,50^FD{0}^FS^XZ".format(data)
            data_bytes = bytes(data, 'UTF-8')
            self_socket.sendall(data_bytes)
            self_socket.close()
            print('Received ', repr(data))
        except self.ConnectionRefusedError as ecx:
            print(ecx.args[1])


    @staticmethod
    def create_zpl(print_string):
        zpl = "^XA^CI15^FO^A0N,50^FD{0}^FS^XZ".format(print_string)
        return zpl


if __name__ == '__main__':
    printer = ZPLPrinter("Printer")
    printer.com_print('com_print')
    printer.net_print('net_print')

import os
import socket

from serial import Serial, SerialException


class ZPLPrinter:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @staticmethod
    def com_print(data):
        serial_port = 'COM7' if os.name == 'nt' else "/dev/ttyS0"
        com_port = Serial(port=serial_port, baudrate=9600, dsrdtr=1, timeout=None)
        try:
            data_bytes = bytes(data, 'UTF-8')
            com_port.write(data_bytes)
            print("\t Sent %s to print" % data)
        except SerialException:
            print('Error in com_print')

    @staticmethod
    def usb_print(data):
        # import usb.core
        # import usb.util
        # dev = usb.core.find(find_all=True)
        pass

    @staticmethod
    def create_zpl(print_string):
        zpl = f"^XA^CI15^FO5,30^ASB,130,130^FD{print_string}^FS^" \
            f"FO295,30^ASR,130,130^FD{print_string}^FS^XZ"
        return zpl

    @staticmethod
    def net_print(data):
        try:
            self_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self_socket.connect(('172.26.193.20', 9100))
            data = "^XA^CI15^FO^A0N,50^FD{0}^FS^XZ".format(data)
            data_bytes = bytes(data, 'UTF-8')
            self_socket.sendall(data_bytes)
            self_socket.close()
            print('Received ', repr(data))
        except ConnectionRefusedError as ecx:
            print(ecx.args[1])


if __name__ == '__main__':
    printer = ZPLPrinter("Printer")
    zpl = printer.create_zpl('206')
    printer.com_print(printer.create_zpl('Test'))

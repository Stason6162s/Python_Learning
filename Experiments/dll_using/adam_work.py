import os
from ctypes import cdll


def adam_init():
    try:
        dll_path = os.path.realpath('Advantech.Adam.dll')
        print(dll_path)
        adam_lib = cdll.LoadLibrary(dll_path)
    except OSError as e:
        print("Error %s " % e)


if __name__ == '__main__':
    adam_init()

'''
adamSocket() = New Advantech.Adam.AdamSocket
adamSocket().Connect(AdamType.Adam5000Tcp, IP, Net.Sockets.ProtocolType.Tcp)
adamSocket().Modbus().ForceSingleCoil(output + 64, value)
adamSocket().Modbus().ReadCoilStatus(1, 64, bdata)
'''

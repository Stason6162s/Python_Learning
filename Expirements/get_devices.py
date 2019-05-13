import os

devices_list = os.popen('driverquery /V').readlines()

print(len(devices_list))

# ghost_devices = []
# for line in devices_list:
#     device_info = line.split()
#     if len(device_info) != 0 and 'Stopped' in device_info:
#         print(device_info)
#         ghost_devices.append(device_info)
# print(len(ghost_devices))

driver_dict = os.popen('pnputil -e').read()
print(driver_dict)
# for value in driver_dict:
#     print(value)
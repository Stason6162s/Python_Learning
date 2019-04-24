def benchmark(func):
    import time

    def wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()
        print("The end wrapper func", end - start)

    return wrapper


def screw_counter(driver_number):
    print('I gotta to be spun %d screws' % driver_number)

@benchmark
def record_torque(driver_number):
    print('I gotta to be record of torques %d' % driver_number)


def scan_bar_code():
    print("I'm scanning the barcode")


if __name__ == '__main__':
    screw_counter(1)
    record_torque(1)
    scan_bar_code()
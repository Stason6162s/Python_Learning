import time


def decorator_function(func):
    def wrapper(*args):
        print('Start the wrapper function')
        print('[*] Start wrapped func()')
        func(*args)
        print('[*] End wrapped func()')

    return wrapper


def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('The', func, 'was completed in', end - start, 'seconds')

    return wrapper


@benchmark
def hello_world(*args):
    print('Hello', *args)


if __name__ == '__main__':
    hello_world('Stasyan')

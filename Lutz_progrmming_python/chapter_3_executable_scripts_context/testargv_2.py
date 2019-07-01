#! usr/bin/env python
print('Wait for it...')


def get_opts(argv):
    opts = {}
    while argv:
        if argv[0][0] == '-':
            opts[argv[0]] = argv[1]
            argv = argv[2:]
        else:
            argv = argv[1:]
    return opts


if __name__ == '__main__':
    from sys import argv

    my_args = get_opts(argv)
    if '-i' in my_args:
        print(my_args['-i'])
    print(my_args)
    input()

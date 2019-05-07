"""
Split the strings by pages
"""
import sys


def more(text, num_lines=15):
    lines = text.splitlines()
    while lines:
        chunk = lines[:num_lines]
        lines = lines[num_lines:]
        for line in chunk:
            print(line)
        if lines and input('More?: ') not in ('y', 'Y'):
            break


if __name__ == '__main__':
    more(open(sys.argv[1]).read(), 10)

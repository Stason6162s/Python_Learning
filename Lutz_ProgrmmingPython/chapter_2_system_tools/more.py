def more(text, num_lines):
    lines = text.splitlines()
    while lines:
        chunk = lines[:num_lines]
        lines = lines[num_lines:]
        for line in chunk:
            print(line)
        if lines and input('More?') not in ['y', 'Y']:
            break


if __name__ == '__main__':
    import sys
    more(open(sys.argv[0]).read(), 15)

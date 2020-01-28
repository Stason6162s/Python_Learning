import os
import sys


def lister(root):
    for (this_dir, subs_here, files_here) in os.walk(root):
        print(f'[{this_dir}]')
        for f_name in files_here:
            print(os.path.join(this_dir, f_name))


if __name__ == '__main__':
    print(sys.argv)
    # lister(sys.argv[0])
    lister('..')

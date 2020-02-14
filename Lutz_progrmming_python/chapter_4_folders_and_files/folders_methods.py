import os
import sys


def lister_walk(root):
    for (this_dir, subs_here, files_here) in os.walk(root):
        print(f'[{this_dir}]')
        for f_name in files_here:
            print(os.path.join(this_dir, f_name))


def lister_mimetype(root):
    matches = []
    for (dir_name, subdir, files_here) in os.walk(root):
        for file_name in files_here:
            if file_name.endswith('.py'):
                path_name = os.path.join(dir_name, file_name)
                if 'mimetypes' in open(path_name).read():
                    matches.append(path_name)
    for name in matches:
        print(name)


if __name__ == '__main__':
    print(sys.argv)
    # lister_walk(sys.argv[0])
    # lister_walk('..')
    lister_mimetype('..')

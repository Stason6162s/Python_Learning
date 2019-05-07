import os

print(list(os.environ.keys()))
print(os.getpid())
print(os.listdir(os.getcwd()))
print('PATH: %s, separator of dirs:%s, pardir:%s, curdir:%s, linesep:%s' % (os.pathsep, os.sep,
                                                                            os.pardir, os.curdir, os.linesep))
print(os.getcwd().split(os.sep))
print('File size is {0} mb'.format(os.path.getsize('more.py')))
print(os.getcwd())
os.chdir(os.path.abspath('..'))
print(os.getcwd())
os.chdir(os.path.abspath(r'chapter_2_system_tools'))
print(os.getcwd())
os.system('dir /B')
os.system('type more.py')
more = os.popen('type more.py').read()
print(more)

os.startfile('string_base.py')

for line in os.popen('dir /B *.py'): print(line)
# So long
# listing = os.popen('dir /B').readlines()
# print(listing)
# files_list = listing
# for file in files_list:
#     os.system('python more.py %s' % file)

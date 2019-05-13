import subprocess

subprocess.call('dir /B', shell=True)  # surely to use shell=True, else FileNotFound exception
subprocess.call('type more.py', shell=True)
subprocess.call('python more.py more.py')  # as a os.system()



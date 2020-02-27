import _thread as thread, time

stdout_mutex = thread.allocate_lock()
exit_mutex = [thread.allocate_lock() for i in range(10)]


def counter(my_id, count):
    for item in range(count):
        stdout_mutex.acquire()
        print(f'[{my_id}] => {item};')
        stdout_mutex.release()
    exit_mutex[my_id].acquire()


for child in range(10):
    thread.start_new_thread(counter, (child, 100))

for mutex in exit_mutex:
    while not mutex.locked():
        time.sleep(1)
        pass
print('Exit from main thread')

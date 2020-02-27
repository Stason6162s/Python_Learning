import _thread as thread, time


def counter(my_id, count):
    for item in range(count):
        time.sleep(1)
        mutex.acquire()
        print(f'[{my_id}] = > {item};')
        mutex.release()

mutex = thread.allocate_lock()
for child in range(5):
    thread.start_new_thread(counter, (child, 5))

time.sleep(6)
print("Exit from main tread")

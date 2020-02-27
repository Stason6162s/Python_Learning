import _thread as thread, time

def count(my_id, count):
    for item in range(count):
        time.sleep(1)
        print(f'[{my_id}] => {item};')


for child in range(5):
    thread.start_new_thread(count, (child, 5))


time.sleep(6)
print('Exit from main thread')
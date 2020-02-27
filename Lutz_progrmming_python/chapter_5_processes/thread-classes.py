import threading


class Mythread(threading.Thread):
    def __init__(self, my_id, count, mutex):
        self.my_id = my_id
        self.count = count
        self.mutex = mutex
        threading.Thread.__init__(self)

    def run(self):
        for i in range(self.count):
            with self.mutex:
                print(f'[{self.my_id}] => {i}')


stdout_mutex = threading.Lock()
threads = []
for child in range(10):
    thread = Mythread(child, 100, stdout_mutex)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
print('End of main thread')
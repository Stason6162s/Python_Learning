num_consumers = 1
num_producers = 4
num_messages = 4

import _thread as thread, queue, time

safe_print = thread.allocate_lock()
data_queue = queue.Queue()


def producer(id_num):
    for msg_num in range(num_messages):
        time.sleep(id_num)
        data_queue.put(f'[producer id = {id_num} count = {msg_num}]')


def consumer(id_num):
    while True:
        time.sleep(0.1)
        try:
            data = data_queue.get(block=False)
        except:
            pass
        else:
            with safe_print:
                print(f'consumer {id_num} got => {data}')


if __name__ == '__main__':
    for i in range(num_consumers):
        thread.start_new_thread(consumer, (i,))
    for i in range(num_producers):
        thread.start_new_thread(producer, (i,))
    time.sleep(((num_producers - 1) * num_messages) + 1)
    print("Main  thread exit")
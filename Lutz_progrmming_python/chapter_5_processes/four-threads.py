"""
4 способа использования потоков
"""
import threading, _thread


# Функция вызываемая в потоках
def action(i):
    print(i ** 32)


# С помощью определения класса потока выполнения
class Mythread(threading.Thread):
    def __init__(self, i):
        self.i = i
        threading.Thread.__init__(self)

    def run(self):
        print(f'Class return {self.i ** 32}')


Mythread(2).start()

# Передача lambda функции
thread = threading.Thread(target=(lambda: action(2)))
thread.start()

# Не используя lambda
threading.Thread(target=action, args=(2,)).start()

# Процедурный метод с помощью _thread
_thread.start_new_thread(action, (2,))

print('Exit from main thread')

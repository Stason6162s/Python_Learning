import sys
import threading
import time

from PyQt5 import QtWidgets, QtCore


def thread(func):
    """
    Decorator for work in the another flow.
    :param func: Function that must to work in a another flow
    :return: Decorator
    """

    def wrapper(*args, **kwargs):
        my_thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        my_thread.start()

    return wrapper


@thread
def processing(signal):
    res = [i for i in 'hello_my_friend']
    time.sleep(2)
    signal.emit(res)


class MyWidget(QtWidgets.QWidget):
    my_signal = QtCore.pyqtSignal(list, name='my_signal')

    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.mainLayout = QtWidgets.QHBoxLayout()
        self.setLayout(self.mainLayout)

        self.button = QtWidgets.QPushButton('Emit your signal', self)
        self.mainLayout.addWidget(self.button)
        self.button.clicked.connect(lambda: processing(self.my_signal))
        self.my_signal.connect(self.my_signal_handler, QtCore.Qt.QueuedConnection)

    def my_signal_handler(self, data):
        print(data)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    app.exec_()

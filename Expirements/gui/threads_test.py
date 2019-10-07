import sys
import time

from PyQt5 import QtWidgets, QtCore


class SlowTask(QtCore.QThread):
    updated = QtCore.pyqtSignal(int)
    running = False

    def __init__(self, *args, **kwargs):
        # super(SlowTask, self).__init__(*args, **kwargs)
        super().__init__()
        self.percent = 0
        self.running = True

    def run(self):
        while self.running:
            self.percent += 1
            self.percent %= 100
            self.updated.emit(int(self.percent))
            time.sleep(0.1)

    def stop(self):
        self.running = False


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Test')
        self.resize(446, 207)

        self.progress_bar = QtWidgets.QProgressBar(self)
        self.progress_bar.setGeometry(QtCore.QRect(40, 70, 381, 23))
        self.progress_bar.setProperty('value', 0)

        self.start_button = QtWidgets.QPushButton('Start', self)
        self.start_button.setGeometry(QtCore.QRect(110, 110, 75, 23))
        self.start_button.setEnabled(True)
        self.start_button.clicked.connect(self.on_start)

        self.stop_button = QtWidgets.QPushButton('Stop', self)
        self.stop_button.setGeometry(QtCore.QRect(260, 110, 75, 23))
        self.stop_button.setEnabled(False)
        self.stop_button.clicked.connect(self.on_stop)

    def toggle_buttons(self):
        self.start_button.setEnabled(not self.start_button.isEnabled())
        self.stop_button.setEnabled(not self.stop_button.isEnabled())

    def on_update(self, data):
        self.progress_bar.setValue(data)
        # if data == 99:
        #     self.on_stop()

    def on_start(self):
        print('Start was pushed')
        self.toggle_buttons()
        self.task = SlowTask(self)
        self.task.updated.connect(self.on_update)
        self.task.start()

    def on_stop(self):
        print('Stop was pushed')
        self.task.stop()
        self.progress_bar.setValue(0)
        self.toggle_buttons()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

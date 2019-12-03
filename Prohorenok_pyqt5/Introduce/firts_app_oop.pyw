import sys

from PyQt5 import QtWidgets


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel("<center>Hello World!</center>")
        # self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.quit_btn = QtWidgets.QPushButton("&Close the window")
        self.v_box = QtWidgets.QVBoxLayout()
        self.v_box.addWidget(self.label)
        self.v_box.addWidget(self.quit_btn)
        self.setLayout(self.v_box)
        self.quit_btn.clicked.connect(QtWidgets.qApp.quit)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("First OOP window")
    window.resize(300, 75)
    window.show()
    sys.exit(app.exec_())

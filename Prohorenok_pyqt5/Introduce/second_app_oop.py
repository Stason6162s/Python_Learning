from PyQt5 import QtWidgets

from Prohorenok_pyqt5.Introduce.firts_app_oop import MyWindow


class MyDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.my_widget = MyWindow()
        self.my_widget.setContentsMargins(0, 0, 0, 0)
        self.change_button = QtWidgets.QPushButton("C&hange text")
        main_box = QtWidgets.QVBoxLayout()
        main_box.addWidget(self.my_widget)
        main_box.addWidget(self.change_button)
        self.setLayout(main_box)
        self.change_button.clicked.connect(self.on_button)

    def on_button(self):
        self.my_widget.label.setText("New text message")
        self.change_button.setDisabled(True)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyDialog()
    window.setWindowTitle('OOP style benefit')
    window.resize(300, 100)
    window.show()
    sys.exit(app.exec_())

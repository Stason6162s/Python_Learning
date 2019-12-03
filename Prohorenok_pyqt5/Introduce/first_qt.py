import sys

from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('First program on PyQt5')
window.resize(300, 70)
label_H = QtWidgets.QLabel('<center> Hello World! </center>')
label_B = QtWidgets.QLabel('<center> Bye World! </center>')
quit_btn = QtWidgets.QPushButton("&Close the window")
labels = [label_H, label_B]
v_box = QtWidgets.QVBoxLayout()
for lbl in labels:
    v_box.addWidget(lbl)
v_box.addWidget(quit_btn)
window.setLayout(v_box)
quit_btn.clicked.connect(app.quit)
window.show()
sys.exit(app.exec_())

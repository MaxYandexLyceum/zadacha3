import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QLCDNumber
import random


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.do_paint = True

    def initUI(self):
        self.setGeometry(0, 0, 2500, 1500)
        self.btn = QPushButton("Окружность", self)
        self.btn.move(30, 50)
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        x = random.randint(1, 1000)
        y = random.randint(1, 1000)
        a = random.randint(1, 300)
        r = random.randint(1, 255)
        g = random.randint(1, 255)
        b = random.randint(1, 255)
        qp.setPen(QColor(r, g, b))
        qp.drawEllipse(x, y, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

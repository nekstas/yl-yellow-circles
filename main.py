# -*- coding: utf-8 -*-
# Автор: Некрасов Станислав
import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class Window(QMainWindow):
    button: QPushButton
    clicked: bool

    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.program_init()

    def program_init(self):
        self.clicked = False
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        self.clicked = True
        self.repaint()

    def paintEvent(self, _):
        if not self.clicked:
            return

        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(0, 0, 0, 0))
        qp.setPen(QColor(255, 255, 0))

        for _ in range(random.randint(2, 11)):
            r = random.randint(1, 100)
            x = random.randint(r, 640 - r)
            y = random.randint(r, 480 - r)
            qp.drawEllipse(x - r, y - r, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())

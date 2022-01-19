import sys

from PyQt6 import QtWidgets
from PyQt6.QtGui import QFont

from app.MainWindow import MainWindow


def main():
    app = QtWidgets.QApplication([])
    app.setFont(QFont("Fantasy"))
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

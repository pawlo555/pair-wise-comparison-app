import sys

from PyQt6 import QtWidgets
from app.MainWindow import MainWindow


def main():
    app = QtWidgets.QApplication([])
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

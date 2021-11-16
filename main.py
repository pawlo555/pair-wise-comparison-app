import sys
from PyQt6 import QtWidgets

from PairWiseComparisonApp.app.app import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MainWindow()
    widget.window().show()

    sys.exit(app.exec())

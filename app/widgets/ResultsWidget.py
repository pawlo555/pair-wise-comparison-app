from PyQt6 import QtCore
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel


class ResultsWidget(QWidget):
    """
        Widget to present results
    """
    def __init__(self, parent, dataManager):
        super().__init__(parent)

        self.dataManager = dataManager
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addStretch(1)

        # Title
        titleLabel = QLabel(self)
        titleLabel.setFont(QFont("SansSerif", 20))
        titleLabel.setText("Results")
        titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(titleLabel)

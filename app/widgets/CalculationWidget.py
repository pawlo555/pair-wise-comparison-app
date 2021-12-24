from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton


class CalculationWidget(QWidget):
    """
        Widget to calculate ranking
    """

    def __init__(self, parent, dataManager, nextLayoutTrigger):
        super().__init__(parent)

        self.dataManager = dataManager

        self.mainLayout = QVBoxLayout()
        self.HLayout = QHBoxLayout()
        self.mainLayout.addStretch()
        self.HLayout.addStretch()

        # Title
        titleLabel = QLabel(self)
        titleLabel.setObjectName("titleLabel")
        titleLabel.setText("Pick ranking method")
        titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(titleLabel)

        # Next stage button
        self.method0 = QPushButton("EVM Method", self)
        self.method0.clicked.connect(lambda: nextLayoutTrigger("EVM"))
        self.HLayout.addWidget(self.method0)

        self.method1 = QPushButton("GMM Method", self)
        self.method1.clicked.connect(lambda: nextLayoutTrigger("GMM"))
        self.HLayout.addWidget(self.method1)

        self.HLayout.addStretch()
        self.mainLayout.addLayout(self.HLayout)
        self.mainLayout.addStretch()
        self.setLayout(self.mainLayout)

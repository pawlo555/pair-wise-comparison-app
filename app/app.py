from PyQt6 import QtWidgets
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QWidget, QVBoxLayout

from PairWiseComparisonApp.app.stages.stageManager import StageManager


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kox apka")
        self.setMinimumSize(QSize(640, 480))

        self.centralWidget = QWidget()
        self.centralLayout = QVBoxLayout()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.centralLayout)

        self.stageManager = StageManager(self.centralWidget)
        self.centralLayout.add(self.stageWidget)
        self.stageManager.setNextStage()

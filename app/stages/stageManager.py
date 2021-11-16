from PyQt6.QtWidgets import QWidget

from PairWiseComparisonApp.app.backend.APIManager import APIManager
from PairWiseComparisonApp.app.backend.dataManager import DataManager


class StageManager:
    def __init__(self, parent: QWidget):
        self.parent = parent
        self.dataManager = DataManager()
        self.APIManager = APIManager()

    def setNextStage(self):
        self.parent.layout().addWidget()

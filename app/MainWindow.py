from PyQt6 import QtWidgets
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QStackedLayout

from PairWiseComparisonApp.app.backend.data_manager import DataManager
from PairWiseComparisonApp.app.widgets.ComplexCriteriaAddWidget import ComplexCriteriaAddWidget
from PairWiseComparisonApp.app.widgets.CriteriaAddWidget import CriteriaAddWidget
from PairWiseComparisonApp.app.widgets.ExpertAddWidget import ExpertAddWidget
from PairWiseComparisonApp.app.widgets.MovieAddWidget import MovieAddWidget
from PairWiseComparisonApp.app.widgets.MoviesRateWidget import MoviesRateWidget


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.dataManager = DataManager()

        self.setWindowTitle("Kox apka")
        self.setMinimumSize(QSize(640, 480))

        self.centralWidget = QWidget()
        self.centralLayout = QHBoxLayout()

        # Widgets for stackedLayout - we can swap between them
        self.stackedLayout = QStackedLayout()
        self.movieAddWidget = MovieAddWidget(self, self.dataManager, self.setNextLayout)
        self.criteriaAddWidget = CriteriaAddWidget(self, self.dataManager, self.setNextLayout)
        self.complexCriteriaAddWidget = ComplexCriteriaAddWidget(self, self.dataManager, self.setNextLayout)
        self.expertAddWidget = ExpertAddWidget(self, self.dataManager, self.setNextLayout)
        self.moviesRateWidget = MoviesRateWidget(self, self.dataManager, self.setNextLayout)

        self.stackedLayout.addWidget(self.movieAddWidget)
        self.stackedLayout.addWidget(self.criteriaAddWidget)
        self.stackedLayout.addWidget(self.complexCriteriaAddWidget)
        self.stackedLayout.addWidget(self.expertAddWidget)
        self.stackedLayout.addWidget(self.moviesRateWidget)

        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.stackedLayout)

    def setNextLayout(self, index: int):
        self.stackedLayout.setCurrentIndex(index)

from PyQt6 import QtWidgets
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QStackedLayout

from app.backend.data_manager import DataManager
from app.widgets.ComplexCriteriaAddWidget import ComplexCriteriaAddWidget
from app.widgets.CriteriaAddWidget import CriteriaAddWidget
from app.widgets.ExpertAddWidget import ExpertAddWidget
from app.widgets.MovieAddWidget import MovieAddWidget
from app.widgets.MoviesRateWidget import MoviesRateWidget

from PairWiseComparisonApp.app.widgets.CalculationWidget import CalculationWidget
from PairWiseComparisonApp.app.widgets.CriteriaRateWidget import CriteriaRateWidget
from PairWiseComparisonApp.app.widgets.ResultsWidget import ResultsWidget


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
        self.expertAddWidget = ExpertAddWidget(self, self.dataManager, self.expertAddNextLayout)
        self.moviesRateWidget = MoviesRateWidget(self, self.dataManager, self.rateMoviesNextLayout)
        self.criteriaRateWidget = CriteriaRateWidget(self, self.dataManager, self.setNextLayout)
        self.calculationWidget = CalculationWidget(self, self.dataManager, self.calculationNextLayout)
        self.resultsWidget = ResultsWidget(self, self.dataManager)

        self.stackedLayout.addWidget(self.movieAddWidget)
        self.stackedLayout.addWidget(self.criteriaAddWidget)
        self.stackedLayout.addWidget(self.complexCriteriaAddWidget)
        self.stackedLayout.addWidget(self.expertAddWidget)
        self.stackedLayout.addWidget(self.moviesRateWidget)
        self.stackedLayout.addWidget(self.criteriaRateWidget)
        self.stackedLayout.addWidget(self.calculationWidget)
        self.stackedLayout.addWidget(self.resultsWidget)

        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.stackedLayout)

    def setNextLayout(self, index: int):
        self.stackedLayout.setCurrentIndex(index)

    def expertAddNextLayout(self):
        self.dataManager.initialize_matrices()
        self.moviesRateWidget.update_layout()
        self.setNextLayout(4)

    def rateMoviesNextLayout(self):
        self.criteriaRateWidget.update_layout()
        self.setNextLayout(5)

    def calculationNextLayout(self, method: str):
        self.dataManager.set_method(method)
        self.dataManager.calc_results()
        self.resultsWidget.updateLayout()
        self.setNextLayout(7)


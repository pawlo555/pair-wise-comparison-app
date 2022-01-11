from PyQt6 import QtWidgets
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QStackedLayout
from app.backend.data_manager import DataManager
from app.styling.styles import setAppStylesheet
from app.widgets.CalculationWidget import CalculationWidget
from app.widgets.ComplexCriteriaAddWidget import ComplexCriteriaAddWidget
from app.widgets.CriteriaAddWidget import CriteriaAddWidget
from app.widgets.CriteriaRateWidget import CriteriaRateWidget
from app.widgets.ExpertAddWidget import ExpertAddWidget
from app.widgets.MovieAddWidget import MovieAddWidget
from app.widgets.MoviesRateWidget import MoviesRateWidget
from app.widgets.ResultsWidget import ResultsWidget


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kox apka")
        self.setBaseSize(QSize(640, 210))
        setAppStylesheet(self)

        self.dataManager = DataManager()

        self.centralWidget = QWidget()
        self.centralWidget.setObjectName("centralWidget")
        self.centralLayout = QHBoxLayout()

        # Widgets for stackedLayout - we can swap between them
        self.stackedLayout = QStackedLayout()
        self.movieAddWidget = MovieAddWidget(self, self.dataManager, self._setNextLayout)
        self.criteriaAddWidget = CriteriaAddWidget(self, self.dataManager, self._criteriaAddNextLayout)
        self.complexCriteriaAddWidget = ComplexCriteriaAddWidget(self, self.dataManager, self._setNextLayout)
        self.expertAddWidget = ExpertAddWidget(self, self.dataManager, self._expertAddNextLayout)
        self.moviesRateWidget = MoviesRateWidget(self, self.dataManager, self._rateMoviesNextLayout)
        self.criteriaRateWidget = CriteriaRateWidget(self, self.dataManager, self._setNextLayout)
        self.calculationWidget = CalculationWidget(self, self.dataManager, self._calculationNextLayout)
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

    def _setNextLayout(self, index: int):
        self.stackedLayout.setCurrentIndex(index)

    def _criteriaAddNextLayout(self):
        self.complexCriteriaAddWidget.updateLayout()
        self._setNextLayout(2)

    def _expertAddNextLayout(self):
        self.dataManager.initialize_matrices()
        self.moviesRateWidget.updateLayout()
        self._setNextLayout(4)

    def _rateMoviesNextLayout(self):
        self.criteriaRateWidget.updateLayout()
        self._setNextLayout(5)

    def _calculationNextLayout(self, method: str):
        self.dataManager.set_method(method)
        self.dataManager.calc_results()
        self.resultsWidget.updateLayout()
        self._setNextLayout(7)


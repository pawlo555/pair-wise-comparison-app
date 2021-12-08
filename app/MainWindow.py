from PyQt6 import QtWidgets
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QStackedLayout

from app.layouts.MenuLayout import MenuLayout
from app.layouts.MovieAddLayout import MovieAddLayout
from app.layouts.GradingLayout import GradingLayout
from app.layouts.ResultsLayout import ResultsLayout
from app.layouts.CriteriaLayout import CriteriaLayout


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kox apka")
        self.setMinimumSize(QSize(640, 480))

        self.centralWidget = QWidget()
        self.centralLayout = QHBoxLayout()

        # Widgets for stackedLayout - we can swap between them
        self.stackedLayout = QStackedLayout()
        self.addMovieWidget = QWidget()
        self.addMovieWidget.setLayout(MovieAddLayout())
        self.criteriaWidget = QWidget()
        self.criteriaWidget.setLayout(CriteriaLayout())
        self.gradingWidget = QWidget()
        self.gradingWidget.setLayout(GradingLayout())
        self.resultsWidget = QWidget()
        self.resultsWidget.setLayout(ResultsLayout())

        self.stackedLayout.addWidget(self.addMovieWidget)
        self.stackedLayout.addWidget(self.criteriaWidget)
        self.stackedLayout.addWidget(self.gradingWidget)
        self.stackedLayout.addWidget(self.resultsWidget)

        self.centralLayout.addLayout(MenuLayout(self))
        self.centralLayout.addLayout(self.stackedLayout)

        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.centralLayout)

    def changeMainLayout(self, index: int):
        self.stackedLayout.setCurrentIndex(index)

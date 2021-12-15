from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QListWidget, QListWidgetItem, \
    QLineEdit, QTableView, QTableWidget, QMessageBox, QTableWidgetItem


class MoviesRateWidget(QWidget):
    """
        Widget to rate movies by every criteria
    """
    def __init__(self, parent, dataManager, nextLayoutTrigger):
        super().__init__(parent)

        self.pickedExpert = None
        self.pickedCriterion = None
        self.criterionMatrix = None
        self.dataManager = dataManager
        self.isRendering = False

        self.mainLayout = QVBoxLayout()
        self.VListLayout = QVBoxLayout()
        self.VRankingLayout = QVBoxLayout()
        self.HLayout = QHBoxLayout()

        self.mainLayout.addStretch(1)
        self.VListLayout.addStretch()
        self.VRankingLayout = QVBoxLayout()

        # Title
        titleLabel = QLabel(self)
        titleLabel.setFont(QFont("Arial", 20))
        titleLabel.setText("Pick criterion to rate movies")
        titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(titleLabel)

        # List of experts
        self.expertsList = QListWidget(self)
        self.expertsList.itemClicked.connect(self.expertChosen)
        self.VListLayout.addWidget(self.expertsList)

        # List of criteria
        self.criteriaList = QListWidget(self)
        self.criteriaList.itemClicked.connect(self.criterionChosen)
        self.VListLayout.addWidget(self.criteriaList)

        self.HLayout.addLayout(self.VListLayout)

        # Movies properties
        self.moviesProperties = QLabel(self)
        self.moviesProperties.setWordWrap(True)
        self.VRankingLayout.addWidget(self.moviesProperties)

        # Ranking Matrix
        self.rankingMatrix = QTableWidget()
        self.rankingMatrix.cellChanged.connect(self.updateDF)

        self.VRankingLayout.addWidget(self.rankingMatrix)
        self.VRankingLayout.addStretch()
        self.HLayout.addLayout(self.VRankingLayout)
        self.mainLayout.addLayout(self.HLayout)

        # Next stage button
        self.nextButton = QPushButton("Next stage", self)
        self.nextButton.clicked.connect(lambda: nextLayoutTrigger())
        self.mainLayout.addWidget(self.nextButton)
        self.mainLayout.addStretch(2)

        self.setLayout(self.mainLayout)

    def updateDF(self, r, c):
        if self.isRendering:
            return

        if r == c:
            self.rankingMatrix.item(r, c).setText("1.0")
            return

        self.criterionMatrix.iloc[r][c] = float(self.rankingMatrix.item(r, c).text())
        self.criterionMatrix.iloc[c][r] = round(1 / float(self.rankingMatrix.item(r, c).text()), 3)
        self.renderRankingMatrix()

    def update_layout(self):
        criteria_list = self.dataManager.get_movie_criteria()
        for criterion in criteria_list:
            self.criteriaList.addItem(QListWidgetItem(criterion))

        expert_list = self.dataManager.get_experts_list()
        for expert in expert_list:
            self.expertsList.addItem(QListWidgetItem(expert))

    def criterionChosen(self, item):
        self.pickedCriterion = item.text()
        self.updateRanking()

    def expertChosen(self, item):
        self.pickedExpert = item.text()
        self.updateRanking()

    def updateRanking(self):
        if self.pickedCriterion is None or self.pickedExpert is None:
            self.showNotEnoughDataError()
        else:
            self.criterionMatrix = self.dataManager.get_criterion_matrix(self.pickedCriterion, self.pickedExpert)
            info = f"Expert {self.pickedExpert} ranks based on {self.pickedCriterion}\n\n"
            for movie in self.dataManager.get_movies_list():
                movieDict = self.dataManager.get_movie_info(movie)
                info += f"{movie}: {movieDict[self.pickedCriterion]}\n"
            self.moviesProperties.setText(info)

            self.renderRankingMatrix()

    def renderRankingMatrix(self):
        self.isRendering = True
        w, h = self.criterionMatrix.shape
        self.rankingMatrix.setRowCount(h)
        self.rankingMatrix.setColumnCount(w)
        self.rankingMatrix.setVerticalHeaderLabels(self.criterionMatrix.columns)
        self.rankingMatrix.setHorizontalHeaderLabels(self.criterionMatrix.columns)

        for c in range(w):
            for r in range(h):
                item = QTableWidgetItem()
                item.setText(f"{self.criterionMatrix.iloc[r][c]}")
                self.rankingMatrix.setItem(r, c, item)
        self.isRendering = False

    def showNotEnoughDataError(self):
        movieErrorDialog = QMessageBox(self)
        movieErrorDialog.setText("Pick user and criterion before rating")
        movieErrorDialog.setWindowTitle("Error")
        movieErrorDialog.show()

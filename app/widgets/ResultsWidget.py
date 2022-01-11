import pandas as pd

from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QListWidget, QListWidgetItem, QTableWidget, \
    QTableWidgetItem

SUMMARISED_RESULTS: str = "Summarised results"


class ResultsWidget(QWidget):
    """
        Widget to show results
    """

    def __init__(self, parent, dataManager):
        super().__init__(parent)

        self.pickedExpert = None
        self.pickedCriterion = None
        self.criterionMatrix = None
        self.isRendering = False
        self.dataManager = dataManager

        self.mainLayout = QVBoxLayout()
        self.VListLayout = QVBoxLayout()
        self.VRankingLayout = QVBoxLayout()
        self.HLayout = QHBoxLayout()
        self.VRankingLayout = QVBoxLayout()

        # Title
        titleLabel = QLabel(self)
        titleLabel.setObjectName("titleLabel")
        titleLabel.setText("results 🏆")
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

        # Ranking info
        self.rankingInfo = QLabel(self)
        self.VRankingLayout.addWidget(self.rankingInfo)

        # Ranking Matrix
        self.rankingMatrix = QTableWidget()
        self.rankingMatrix.cellChanged.connect(self.updateDF)

        self.VRankingLayout.addWidget(self.rankingMatrix)
        self.HLayout.addLayout(self.VRankingLayout)
        self.mainLayout.addLayout(self.HLayout)

        self.setLayout(self.mainLayout)

    def updateLayout(self):
        criteria_list = self.dataManager.get_picked_criteria_list()
        for criterion in criteria_list:
            self.criteriaList.addItem(QListWidgetItem(criterion))

        expert_list = self.dataManager.get_experts_list()
        self.expertsList.addItem(QListWidgetItem(SUMMARISED_RESULTS))
        for expert in expert_list:
            self.expertsList.addItem(QListWidgetItem(expert))

    def criterionChosen(self, item):
        self.pickedCriterion = item.text()
        self.updateRanking()

    def expertChosen(self, item):
        self.pickedExpert = item.text()
        self.updateRanking()

    def updateDF(self, r, c):
        if self.isRendering:
            return

        self.rankingMatrix.item(r, c).setText(f"{self.criterionMatrix.iloc[r][c]}")
        self.renderRankingMatrix()

    def updateRanking(self):
        if self.pickedCriterion and self.pickedExpert:
            expert = None if self.pickedExpert == SUMMARISED_RESULTS else self.pickedExpert
            inconsistencyInfo = f"\n inconsistency ratio: {self.dataManager.get_inconsistency(self.pickedCriterion, expert)}" if expert else ""
            data = self.dataManager.get_result_matrix(self.pickedCriterion, expert)
            names = self.dataManager.get_movies_list()
            self.criterionMatrix = pd.DataFrame(data=data, columns=names, index=[self.pickedCriterion])

            self.rankingInfo.setText(f"ranking based on {self.pickedCriterion} {inconsistencyInfo}")
            self.renderRankingMatrix()

    def renderRankingMatrix(self):
        self.isRendering = True
        w, h = self.criterionMatrix.shape
        self.rankingMatrix.setRowCount(h)
        self.rankingMatrix.setColumnCount(w)
        self.rankingMatrix.setVerticalHeaderLabels(self.criterionMatrix.columns)
        self.rankingMatrix.setHorizontalHeaderLabels([self.pickedCriterion])

        for c in range(h):
            for r in range(w):
                item = QTableWidgetItem()
                item.setText(f"{round(self.criterionMatrix.iloc[r][c], 3)}")
                self.rankingMatrix.setItem(r, c, item)
        self.isRendering = False

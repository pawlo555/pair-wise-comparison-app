from PyQt6 import QtCore

from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QListWidget, QListWidgetItem, QTableWidget, QMessageBox, QTableWidgetItem

# TODO: Change criteria list
from PairWiseComparisonApp.app.widgets.ScrollableLabel import ScrollableLabel


class CriteriaRateWidget(QWidget):
    """
        Widget to rate importance of criteria
    """
    def __init__(self, parent, dataManager, nextLayoutTrigger):
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
        titleLabel.setText("criteria rate time ⏱")
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
        self.rankingInfo = ScrollableLabel(self)
        self.VRankingLayout.addWidget(self.rankingInfo, stretch=1)

        # Ranking Matrix
        self.rankingMatrix = QTableWidget()
        self.rankingMatrix.cellChanged.connect(self.updateDF)

        self.VRankingLayout.addWidget(self.rankingMatrix, stretch=3)
        self.HLayout.addLayout(self.VRankingLayout, stretch=5)
        self.mainLayout.addLayout(self.HLayout)

        # Next stage button
        self.nextButton = QPushButton("next stage", self)
        self.nextButton.clicked.connect(lambda: nextLayoutTrigger(6))
        nextButtonLayout = QHBoxLayout()
        nextButtonLayout.addStretch(1)
        nextButtonLayout.addWidget(self.nextButton)
        nextButtonLayout.addStretch(1)
        self.mainLayout.addLayout(nextButtonLayout)

        self.setLayout(self.mainLayout)

    def update_layout(self):
        criteria_list = self.dataManager.get_complex_criteria()
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

    def updateDF(self, r, c):
        if self.isRendering:
            return

        if r == c:
            self.rankingMatrix.item(r, c).setText("1.0")
            return

        self.criterionMatrix.iloc[r][c] = float(self.rankingMatrix.item(r, c).text())
        self.criterionMatrix.iloc[c][r] = round(1 / float(self.rankingMatrix.item(r, c).text()), 3)
        self.renderRankingMatrix()

    def updateRanking(self):
        if self.pickedCriterion is None or self.pickedExpert is None:
            return
        else:
            self.criterionMatrix = self.dataManager.get_criterion_matrix(self.pickedCriterion, self.pickedExpert)
            self.rankingInfo.setText(f"🧐 expert {self.pickedExpert} ranks {self.pickedCriterion}")
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

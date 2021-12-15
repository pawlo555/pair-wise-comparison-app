from PyQt6 import QtCore
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QListWidget, QListWidgetItem, QTableWidget, QMessageBox, QTableWidgetItem

# TODO: Change criteria list


class CriteriaRateWidget(QWidget):
    """
        Widget to rate importance of criteria
    """
    def __init__(self, parent, dataManager, nextLayoutTrigger):
        super().__init__(parent)

        self.pickedExpert = None
        self.pickedCriterion = None
        self.criterionMatrix = None
        self.dataManager = dataManager

        self.mainLayout = QVBoxLayout()
        self.VLayout = QVBoxLayout()
        self.HLayout = QHBoxLayout()

        self.mainLayout.addStretch(1)
        self.VLayout.addStretch()

        # Title
        titleLabel = QLabel(self)
        titleLabel.setFont(QFont("Arial", 20))
        titleLabel.setText("Pick criteria to rank their importance")
        titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(titleLabel)

        # List of experts
        self.expertsList = QListWidget(self)
        self.expertsList.itemClicked.connect(self.expertChosen)
        self.VLayout.addWidget(self.expertsList)

        # List of criteria
        self.criteriaList = QListWidget(self)
        self.criteriaList.itemClicked.connect(self.criterionChosen)
        self.VLayout.addWidget(self.criteriaList)

        self.HLayout.addLayout(self.VLayout)

        # Ranking Matrix
        self.rankingMatrix = QTableWidget()
        movies = self.dataManager.get_movies_list()
        self.rankingMatrix.setVerticalHeaderLabels(movies)
        self.rankingMatrix.setHorizontalHeaderLabels(movies)
        self.HLayout.addWidget(self.rankingMatrix)
        self.mainLayout.addLayout(self.HLayout)

        # Next stage button
        self.nextButton = QPushButton("Next stage", self)
        self.nextButton.clicked.connect(lambda: nextLayoutTrigger(6))
        self.mainLayout.addWidget(self.nextButton)
        self.mainLayout.addStretch(2)

        self.setLayout(self.mainLayout)

    def update_layout(self):
        criteria_list = self.dataManager.get_picked_criteria_list()
        for criterion in criteria_list:
            self.criteriaList.addItem(QListWidgetItem(criterion))

        expert_list = self.dataManager.get_experts_list()
        for expert in expert_list:
            self.expertsList.addItem(QListWidgetItem(expert))

    def criterionChosen(self, item):
        self.pickedCriterion = item.text()
        if self.pickedCriterion is None or self.pickedExpert is None:
            self.showNotEnoughDataError()
        else:
            self.criterionMatrix = self.dataManager.get_criterion_matrix(self.pickedCriterion, self.pickedExpert)
            self.renderRankingMatrix()

    def expertChosen(self, item):
        self.pickedExpert = item.text()
        if self.pickedCriterion is None or self.pickedExpert is None:
            self.showNotEnoughDataError()
        else:
            self.criterionMatrix = self.dataManager.get_criterion_matrix(self.pickedCriterion, self.pickedExpert)
            self.renderRankingMatrix()

    def renderRankingMatrix(self):
        w, h = self.criterionMatrix.shape
        self.rankingMatrix.setRowCount(h)
        self.rankingMatrix.setColumnCount(w)

        for c in range(w):
            for r in range(h):
                item = QTableWidgetItem(self.criterionMatrix[r][c])
                self.rankingMatrix.setItem(r, c, item)

    def showNotEnoughDataError(self):
        movieErrorDialog = QMessageBox(self)
        movieErrorDialog.setText("Pick user and criterion before rating")
        movieErrorDialog.setWindowTitle("Error")
        movieErrorDialog.show()

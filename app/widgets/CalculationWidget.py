from PyQt6 import QtCore
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QListWidget, QListWidgetItem, \
    QLineEdit, QTableView, QTableWidget, QMessageBox, QTableWidgetItem


class CalculationWidget(QWidget):
    """
        Widget to calculate ranking
    """
    def __init__(self, parent, dataManager, nextLayoutTrigger):
        super().__init__(parent)

        self.dataManager = dataManager

        self.mainLayout = QVBoxLayout()
        self.HLayout = QHBoxLayout()
        self.mainLayout.addStretch()
        self.HLayout.addStretch()

        # Title
        titleLabel = QLabel(self)
        titleLabel.setFont(QFont("Arial", 20))
        titleLabel.setText("Pick ranking method")
        titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(titleLabel)

        # Next stage button
        self.method0 = QPushButton("EVM Method", self)
        self.method0.clicked.connect(lambda: nextLayoutTrigger("EVM"))
        self.HLayout.addWidget(self.method0)

        self.method1 = QPushButton("GMM Method", self)
        self.method1.clicked.connect(lambda: nextLayoutTrigger("GMM"))
        self.HLayout.addWidget(self.method1)

        self.HLayout.addStretch()
        self.mainLayout.addLayout(self.HLayout)
        self.mainLayout.addStretch()
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

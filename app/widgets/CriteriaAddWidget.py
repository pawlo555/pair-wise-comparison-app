from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QListWidget, QListWidgetItem


class CriteriaAddWidget(QWidget):
    """
        Widget to add new criteria
    """

    def __init__(self, parent, dataManager, nextLayoutTrigger):
        super().__init__(parent)

        self.dataManager = dataManager
        self.mainLayout = QVBoxLayout()
        self.tablesLayout = QHBoxLayout()
        # self.mainLayout.addStretch(1)

        # Title
        titleLabel = QLabel(self)
        titleLabel.setObjectName("titleLabel")
        titleLabel.setText("pick something you care about 💕")
        titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(titleLabel)

        # List of all criteria
        self.allCriteria = QListWidget(self)
        self.allCriteria.itemClicked.connect(self.allCriteriaClicked)

        criteria_list = self.dataManager.get_all_criteria_list()
        for criterion in criteria_list:
            self.allCriteria.addItem(QListWidgetItem(criterion))

        self.tablesLayout.addWidget(self.allCriteria)

        # List of picked criteria
        self.pickedCriteria = QListWidget(self)
        self.pickedCriteria.itemClicked.connect(self.pickedCriteriaClicked)
        self.tablesLayout.addWidget(self.pickedCriteria)
        self.mainLayout.addLayout(self.tablesLayout)

        # Next stage button
        self.nextButton = QPushButton("next stage", self)
        self.nextButton.clicked.connect(lambda: nextLayoutTrigger())
        nextButtonLayout = QHBoxLayout()
        nextButtonLayout.addStretch(1)
        nextButtonLayout.addWidget(self.nextButton)
        nextButtonLayout.addStretch(1)
        self.mainLayout.addLayout(nextButtonLayout)
        # self.mainLayout.addStretch(2)

        self.setLayout(self.mainLayout)

    def allCriteriaClicked(self, item):
        self.dataManager.add_criterion(item.text())
        self.renderPickedCriteriaList()

    def pickedCriteriaClicked(self, item):
        self.dataManager.remove_criterion(item.text())
        self.renderPickedCriteriaList()

    def renderPickedCriteriaList(self):
        picked_criteria_list = self.dataManager.get_movie_criteria()
        self.pickedCriteria.clear()

        for criterion in picked_criteria_list:
            self.pickedCriteria.addItem(QListWidgetItem(criterion))

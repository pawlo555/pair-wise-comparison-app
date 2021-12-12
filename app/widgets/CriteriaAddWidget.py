from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QSizePolicy, \
    QListWidget, QListWidgetItem


class CriteriaAddWidget(QWidget):
    """
        Widget to add new criteria
    """
    def __init__(self, parent, dataManager, nextLayoutTrigger):
        super().__init__(parent)

        self.dataManager = dataManager
        self.mainLayout = QVBoxLayout()
        self.tablesLayout = QHBoxLayout()
        self.mainLayout.addStretch(1)
        self.tablesLayout.addStretch()

        # Title
        titleLabel = QLabel(self)
        titleLabel.setFont(QFont("SansSerif", 20))
        titleLabel.setText("Pick crieteria:")
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
        self.tablesLayout.addStretch()
        self.mainLayout.addLayout(self.tablesLayout)

        # Next stage button
        self.nextButton = QPushButton("Next stage", self)
        self.nextButton.clicked.connect(lambda: nextLayoutTrigger(2))
        self.mainLayout.addWidget(self.nextButton)
        self.mainLayout.addStretch(2)

        self.setLayout(self.mainLayout)

    def allCriteriaClicked(self, item):
        self.dataManager.add_criterion(item.text())
        self.renderPickedCriteriaList()

    def pickedCriteriaClicked(self, item):
        self.dataManager.remove_criterion(item.text())
        self.renderPickedCriteriaList()

    def renderPickedCriteriaList(self):
        picked_criteria_list = self.dataManager.get_picked_criteria_list()
        self.pickedCriteria.clear()

        for criterion in picked_criteria_list:
            self.pickedCriteria.addItem(QListWidgetItem(criterion))


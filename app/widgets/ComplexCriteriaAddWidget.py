from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QListWidget, QListWidgetItem, \
    QLineEdit


class ComplexCriteriaAddWidget(QWidget):
    """
        Widget to create complex criteria
    """
    def __init__(self, parent, dataManager, nextLayoutTrigger):
        super().__init__(parent)

        self.dataManager = dataManager
        self.mainLayout = QVBoxLayout()
        self.VLayout = QVBoxLayout()
        self.HLayout = QHBoxLayout()

        # Title
        titleLabel = QLabel(self)
        titleLabel.setObjectName("titleLabel")
        titleLabel.setText("set own ranking rules 🌞")
        titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(titleLabel)

        # List of all criteria
        self.allCriteria = QListWidget(self)
        # TODO: selection mode to enable multiple choice
        # self.allCriteria.setSelectionModel(2)

        criteria_list = self.dataManager.get_all_criteria_list()
        for criterion in criteria_list:
            self.allCriteria.addItem(QListWidgetItem(criterion))

        self.HLayout.addWidget(self.allCriteria)

        # Create new criterion
        self.inputLabel = QLineEdit(self)
        self.inputLabel.setText("type new label...")
        self.VLayout.addWidget(self.inputLabel)
        createButtonLayout = QHBoxLayout()
        createButtonLayout.addStretch()
        self.confirmButton = QPushButton("create", self)
        self.confirmButton.clicked.connect(self.createComplexCriterion)
        createButtonLayout.addWidget(self.confirmButton)
        createButtonLayout.addStretch()
        self.VLayout.addLayout(createButtonLayout)

        self.HLayout.addLayout(self.VLayout)
        self.mainLayout.addLayout(self.HLayout)

        # Next stage button
        self.nextButton = QPushButton("next stage", self)
        self.nextButton.clicked.connect(lambda: nextLayoutTrigger(3))
        nextButtonLayout = QHBoxLayout()
        nextButtonLayout.addStretch(1)
        nextButtonLayout.addWidget(self.nextButton)
        nextButtonLayout.addStretch(1)
        self.mainLayout.addLayout(nextButtonLayout)

        self.setLayout(self.mainLayout)

    def createComplexCriterion(self):
        name = self.inputLabel.text()
        items = self.allCriteria.selectedItems()
        self.dataManager.create_complex_criterion(name, items)

    def renderCriteriaList(self):
        criteria_list = self.dataManager.get_all_criteria_list()
        self.allCriteria.clear()

        for criterion in criteria_list:
            self.allCriteria.addItem(QListWidgetItem(criterion))



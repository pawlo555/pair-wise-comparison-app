from PyQt6 import QtCore
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QListWidget, QListWidgetItem, \
    QLineEdit


class ComplexCriteriaAddWidget(QWidget):
    """
        Widget to add new criteria to movies list
    """
    def __init__(self, parent, dataManager, nextLayoutTrigger):
        super().__init__(parent)

        self.dataManager = dataManager
        self.mainLayout = QVBoxLayout()
        self.VLayout = QVBoxLayout()
        self.HLayout = QHBoxLayout()
        self.mainLayout.addStretch(1)
        self.HLayout.addStretch()
        self.VLayout.addStretch()

        # Title
        titleLabel = QLabel(self)
        titleLabel.setFont(QFont("SansSerif", 20))
        titleLabel.setText("Pick crieteria to create a new complex criterion:")
        titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(titleLabel)

        # List of all criteria
        self.allCriteria = QListWidget(self)
        # TODO: selection mode to enable multiple choice
        # self.allCriteria.setSelectionMode(QAbstractItemView.MultiSelection)

        criteria_list = self.dataManager.get_all_criteria_list()
        for criterion in criteria_list:
            self.allCriteria.addItem(QListWidgetItem(criterion))

        self.HLayout.addWidget(self.allCriteria)

        # Create new criterion
        self.inputLabel = QLineEdit(self)
        self.inputLabel.setText("Type new label...")
        self.VLayout.addWidget(self.inputLabel)

        self.confirmButton = QPushButton("Create", self)
        self.confirmButton.clicked.connect(self.createComplexCriterion)
        self.VLayout.addWidget(self.confirmButton)
        self.VLayout.addStretch()

        self.HLayout.addLayout(self.VLayout)
        self.HLayout.addStretch()
        self.mainLayout.addLayout(self.HLayout)

        # Next stage button
        self.nextButton = QPushButton("Next stage", self)
        self.nextButton.clicked.connect(lambda: nextLayoutTrigger(3))
        self.mainLayout.addWidget(self.nextButton)
        self.mainLayout.addStretch(2)

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



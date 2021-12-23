from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QSizePolicy, \
    QListWidget, QListWidgetItem


class ExpertAddWidget(QWidget):
    """
        Widget to add new expert
    """
    def __init__(self, parent, dataManager, nextLayoutTrigger):
        super().__init__(parent)

        self.dataManager = dataManager
        self.mainLayout = QVBoxLayout()
        self.inputLayout = QHBoxLayout()
        self.mainLayout.addStretch(1)
        self.inputLayout.addStretch()

        # Title
        titleLabel = QLabel(self)
        titleLabel.setObjectName("titleLabel")
        titleLabel.setText("who's the expert here? 😛")
        titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(titleLabel)

        # List of picked movies
        self.expertsList = QListWidget(self)
        self.mainLayout.addWidget(self.expertsList)

        # Input field
        self.input = QLineEdit(self)
        self.inputLayout.addWidget(self.input)

        # Input confirmation button
        self.confirmButton = QPushButton("add", self)
        self.confirmButton.clicked.connect(self.addExpert)
        self.inputLayout.addWidget(self.confirmButton)
        self.inputLayout.addStretch()
        self.mainLayout.addLayout(self.inputLayout)

        # Next stage button
        self.nextButton = QPushButton("next stage", self)
        self.nextButton.clicked.connect(lambda: nextLayoutTrigger())
        nextButtonLayout = QHBoxLayout()
        nextButtonLayout.addStretch(1)
        nextButtonLayout.addWidget(self.nextButton)
        nextButtonLayout.addStretch(1)
        self.mainLayout.addLayout(nextButtonLayout)
        self.mainLayout.addStretch(2)

        self.setLayout(self.mainLayout)

    def addExpert(self):
        newExpert = self.input.text()
        self.dataManager.add_expert(newExpert)
        expertsList = self.dataManager.get_experts_list()
        for expert in expertsList:
            item = QListWidgetItem(expert)
            self.expertsList.addItem(item)



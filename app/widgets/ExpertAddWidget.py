from PyQt6 import QtCore
from PyQt6.QtGui import QFont
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
        titleLabel.setFont(QFont("SansSerif", 20))
        titleLabel.setText("Type new expert profile:")
        titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(titleLabel)

        # List of picked movies
        self.expertsList = QListWidget(self)
        self.mainLayout.addWidget(self.expertsList)

        # Input field
        self.input = QLineEdit(self)
        self.inputLayout.addWidget(self.input)

        # Input confirmation button
        self.confirmButton = QPushButton("Add", self)
        self.confirmButton.clicked.connect(self.addExpert)
        self.inputLayout.addWidget(self.confirmButton)
        self.inputLayout.addStretch()
        self.mainLayout.addLayout(self.inputLayout)

        # Next stage button
        self.nextButton = QPushButton("Next stage", self)
        self.nextButton.clicked.connect(lambda: nextLayoutTrigger(4))
        self.mainLayout.addWidget(self.nextButton)
        self.mainLayout.addStretch(2)

        self.setLayout(self.mainLayout)

    def addExpert(self):
        newExpert = self.input.text()
        self.dataManager.add_expert(newExpert)
        expertsList = self.dataManager.get_experts_list()
        for expert in expertsList:
            item = QListWidgetItem(expert)
            self.expertsList.addItem(item)


